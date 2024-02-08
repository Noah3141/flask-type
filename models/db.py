import json
from typing import Any, Callable, Dict, List, NamedTuple, Type, TypeAlias, TypeVar, TypedDict, Unpack, ParamSpec, get_args
from pydantic import PrivateAttr
from sqlalchemy.orm import DeclarativeBase
from db import Session as SessionMaker
from sqlalchemy.orm import Session

from models.user import User

Output = TypeVar("Output") 
Input = ParamSpec("Input")
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

def decoratorFunctionWithArguments(arg1, arg2, arg3):
    def wrap(f):
        def wrapped_f(*args):
            f(*args)
        return wrapped_f
    return wrap


class Db:
    "Router for Db methods"

    def __init__(self):
        self.session = SessionMaker()
        self.users = UsersRouter(self.session).routes

    def __del__(self):
        self.session.close()

    @staticmethod
    def Router(*args: Callable[Input, Output], decs: List[Callable[[Callable[Input, Output]],  Callable[Input, Output]]] | None = None,) -> Callable[Input, Output]:
        if decs:
            @staticmethod
            def inner(*inner_args: Input.args, **_kwargs: Input.kwargs) -> Output:
                return args[0](*inner_args,  **_kwargs)
        
            for wrapper in decs:
                def inner_wrapped(*inner_args: Input.args, **_kwargs: Input.kwargs) -> Output:
                    output = wrapper(inner, *inner_args, **_kwargs)
                    return output(*inner_args, **_kwargs)
            else:
                raise Exception("Shouldn't ever happen")
        
        else:
            @staticmethod
            def inner_wrapped(*inner_args: Input.args, **_kwargs: Input.kwargs) -> Output:
                return args[0](*inner_args, **_kwargs)
            
        return inner_wrapped

    def RollbackOnFail(self, f: Callable[Input, Output]) -> Callable[Input, Output]:
        def inner(*args: Input.args, **kwargs: Input.kwargs) -> Output:
            try:
                return f(*args, **kwargs)
            except Exception as e:
                self.session.rollback()
                raise e
        return inner
    
    def Log(self, f: Callable[Input, Output]) -> Callable[Input, Output]:
        def inner(*args: Input.args, **kwargs: Input.kwargs) -> Output:
            output = f(*args, **kwargs)
            print(f"{f.__name__} call returning: {json.dumps(output, default=lambda obj: obj.__dict__, indent=3)}")
            return output
            
        return inner

class UsersRouter(Db):
    "Subrouter within Db"
    

    def __init__(self, session: Session):
        self.__session =  session
        Db = super()
        Router = Db.Router

        class UserRoutes:
            @Db.RollbackOnFail
            def get_all() -> List[User]:
                return []
            
            @Db.RollbackOnFail
            @staticmethod
            def first_where(name: str) -> List[User]:
                return []
            
            
            @Router()
            def get_by_name(name: str) -> List[User]:
                return []

            @Router(decs=[Db.RollbackOnFail, Db.Log])
            def get_by_id(id: int) -> List[User]:
                return []
            
        
        self.routes = UserRoutes()

    