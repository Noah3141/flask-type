from typing import NamedTuple
from flask.sessions import SessionMixin as FlaskSession
from sqlalchemy.orm import Session as DbSession
from flask import session
from models.db import Db
from flask import request, Request


# Both SQLAlchemy and Flask having a "session" makes it all the more useful to contextually-wrap and rename with a lightweight class
# ctx.db...
# ctx.session

class Ctx:
    """
        General context object for use in routes. Initializes Db connection and closes in destructor
    """
    session: FlaskSession = session
    "User session"
    db: Db = Db()
    "Database connection"
    request: Request = request
