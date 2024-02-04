from typing import NamedTuple
from flask.sessions import SessionMixin as FlaskSession
from sqlalchemy.orm import Session as DbSession

class Ctx(NamedTuple):
    session: FlaskSession
    "User session"
    db: DbSession
    "Database connection"

