from fastapi_users.db import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)

from .mixins.id_int_pk import IdIntPkMixin
from .base import Base


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    pass
