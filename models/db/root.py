
import json 
from typing import Any, Callable, Dict, List, Literal, NamedTuple, Self, Tuple, Type, TypeAlias, TypeVar, TypedDict, Unpack, ParamSpec, assert_type, get_args
from db import Session as SessionMaker



Output = TypeVar("Output") 
RouterErr = TypeVar("RouterErr")
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
        err: str

    def __init__(self, e: ErrorData):
        self.err = e

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


from typing import Generic



class Ok(NamedTuple, Generic[Output]):
    val: Output
    err: Literal[None] = None

class Err(NamedTuple, Generic[RouterErr]):
    err: RouterError
    val: None = None

RouterOutput = Ok[Output] | Err[RouterError]


def Atomic(*f: Callable[Input, Output]) -> Callable[Input, RouterOutput[Output]]:
    # Make "transaction here?" No session?

    def wrapper(*args: Input.args, **kwargs: Input.kwargs) -> RouterOutput[Output]:
        print("Starting session")
        session = SessionMaker()
        try:
            print("Firing query")
            output: Output = f[0](*args, **kwargs)
            print("Query received")
            session.commit()
            session.close()
            print("Session closed")
            return Ok(output)
        
        except RouterError as e:
            session.rollback()
            session.close()
            return Err(e)

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
