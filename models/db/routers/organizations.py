from typing import List, NamedTuple, Never, TypedDict
from sqlalchemy.orm import Session

from ..root import Atomic, Log, Db, RouterError


class Organization(NamedTuple):
    name: str
    id: int


class OrganizationsRouter:
    "Subrouter within Db"
    
    Router = Db.Router
    def __init__(self, session: Session):
        self.session =  session

    

    class GetById(TypedDict):
        id: int

    @Atomic   
    def get_by_id(self, opts: GetById) -> Organization:
        model = self.session.query(Organization).get(opts["id"])

        if model is None: raise RouterError({"msg":"Not found!"})
        return Organization(
            **model
        )

    def find_all(self) -> List[Organization]:
        return self.session.query(Organization).all()
    
    
