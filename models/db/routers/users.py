from typing import  List
from sqlalchemy.orm import Session

from models.user import User
from ..root import Db, Atomic, Log


class UsersRouter:
    "Subrouter within Db"

    Router = Db.Router

    # @Atomic
    def __init__(self, session: Session):
        self.session = session
    

    def get_all(self) -> List[User]:
        self.session.query
        return []
    
    @staticmethod
    def first_where(name: str) -> List[User]:
        return []
    
    
    # @Router([staticmethod, Atomic,])
    @staticmethod
    def get_by_name(name: str) -> List[User]:
        return []
    
    @staticmethod
    def get_by_id(id: int) -> List[User]:
        return []
    
