from typing import Any, Callable, Dict, List, NamedTuple, Type, TypeAlias, TypeVar, TypedDict, Unpack, ParamSpec
from pydantic import PrivateAttr
from sqlalchemy.orm import DeclarativeBase
from db import Session as SessionMaker
from sqlalchemy.orm import Session

from models.user import User

Output = TypeVar("Output") 
Input = ParamSpec("Input")



class Db:
    "Router for Db methods"

    def __init__(self):
        self.session = SessionMaker()
        self.users = UsersRouter(self.session).methods

    def __del__(self):
        self.session.close()

    def RollbackOnFail(self, f: Callable[Input, Output]) -> Callable[Input, Output]:
        def inner(*args: Input.args, **kwargs: Input.kwargs) -> Output:
            try:
                return f(*args, **kwargs)
            except Exception as e:
                self.session.rollback()
                raise e
        return inner
    

class UsersRouter(Db):
    "Subrouter within Db"
    

    def __init__(self, session: Session):
        self.__session =  session

        class UserMethods:
            @super(UsersRouter).RollbackOnFail
            def get_all() -> List[User]:
                pass
        
        self.methods = UserMethods()