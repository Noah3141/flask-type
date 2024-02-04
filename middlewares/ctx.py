from typing import NamedTuple
from flask.sessions import SessionMixin as FlaskSession
from sqlalchemy.orm import Session as DbSession
from flask import session
from db import Session as Db
from flask import request, Request


class Ctx:
    """
        General context object for use in routes. Initializes Db connection and closes in destructor
    """
    session: FlaskSession = session
    "User session"
    db: DbSession = Db()
    "Database connection"
    request: Request = request
    
    def __del__(self):
        self.db.close()