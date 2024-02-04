from typing import NamedTuple
from sqlalchemy import (
    String, 
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)
from blueprints.admin.users.create_form import CreateUserForm, NonNull

from db import engine
from models import Base


class User(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    nickname: Mapped[str | None] = mapped_column(String(50))
    age: Mapped[int] = mapped_column()

    def __init__(self, form: CreateUserForm):
        if form.validate():
            self.name = form.name.data or ""
            self.nickname = form.nickname or ""
        else:
            raise ValueError("Form")




Base.metadata.create_all(bind=engine)
