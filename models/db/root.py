
import json 
from typing import Any, Callable, Dict, List, Literal, NamedTuple, Self, Tuple, Type, TypeAlias, TypeVar, TypedDict, Unpack, ParamSpec, assert_type, get_args

from db import Session as SessionMaker



Output = TypeVar("Output") 
Input = ParamSpec("Input")

DecOut = TypeVar("DecOut") 
DecInput = ParamSpec("DecInput")
Fn = Callable

Decorator = Fn[
    [Fn[Input, Output]], # Takes in a function
    # Makes a function inside itself using that outer function
    Fn[Input, Output] # Returns the newly made function
    # @ pie syntax means "Pass this function into this decorator, and call the output instead of this function"
]

DecoratorFactory = Fn[
    [
        Fn[Input, Output], 
        List[
            Fn[
                [Fn[Input, Output]],
                Fn[Input, Output]
            ]
        ]
    ],
    Fn[Input, Output]
]
def panic():
    raise Exception("")
# def decoratorFunctionWithArguments(arg1, arg2, arg3):
#     def wrap(f):
#         def wrapped_f(*args):
#             f(*args)
#         return wrapped_f
#     return wrap


class RouterError(Exception):
    class ErrorData(TypedDict):
        msg: str

    def __init__(self, e: ErrorData):
        self.data = e

class Db:
    "Router for Db methods"

    def __init__(self):
        from .routers.users import UsersRouter
        from .routers.organizations import OrganizationsRouter
        
        session = SessionMaker()

        self.users = UsersRouter(session)
        self.organizations = OrganizationsRouter(session)

    
    @staticmethod
    def Router(*arg: Callable[Input, Output], using: List[Callable[[Callable[Input, Output]],  Callable[Input, Output]]],  ) -> Callable[Input, Callable[Input, Output]]:
        
        def decorator(f: Callable[Input, Output]) -> Callable[Input, Output]:
            for d in reversed(using):
                f = d(f)
            return f

        return decorator # type:ignore





def Atomic(*f: Callable[Input, Output]) -> Callable[Input, Tuple[Output, None] | Tuple[RouterError, None]]:
    # Make "transaction here?" No session?

    class RouterErr(NamedTuple):
        err: RouterError
        data: Literal[None] = None

    class RouterOk(NamedTuple):
        data: Output
        err: Literal[None] = None


    def wrapper(*args: Input.args, **kwargs: Input.kwargs) ->  RouterErr | RouterOk:
        print("Starting session")
        session = SessionMaker()
        try:
            print("Firing query")
            output: Output = f[0](*args, **kwargs)
            print("Query received")
            session.commit()
            session.close()
            print("Session closed")
            return RouterOk(output)
        
        except RouterError as e:
            session.rollback()
            session.close()
            return RouterErr(e)

        except Exception as e:
            session.rollback()
            session.close()
            raise e
        

    return wrapper

def Log(*f: Callable[Input, Output]) -> Callable[Input, Output]:
    def inner(*args: Input.args, **kwargs: Input.kwargs) -> Output:
        output = f[0](*args, **kwargs)
        print(f"{f[0].__name__} call returning: {json.dumps(output, default=lambda obj: obj.__dict__, indent=3)}")
        return output
        
    return inner
