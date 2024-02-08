from typing import NamedTuple, TypeVar, cast
from sqlalchemy import (
    String, 
    Integer,
    Boolean
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)
from typings.validation import si, ss
from blueprints.admin.users.create_form import CreateUserForm

from db import engine
from models import Base

class User(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    nickname: Mapped[str | None] = mapped_column(String(50))
    age: Mapped[int | None] = mapped_column(Integer)
    cool: Mapped[bool] = mapped_column(Boolean)

    def __init__(self, form: CreateUserForm):
        self.name = ss(form.name.data)
        self.nickname = form.nickname.data
        self.age = si(form.age.data)
        self.cool = form.cool.data


Base.metadata.create_all(bind=engine)


