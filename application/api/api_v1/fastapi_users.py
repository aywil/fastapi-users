from fastapi_users import FastAPIUsers

from core.types import UserIdType
from core.models import User

from api.dependencies.authentication.user_manager import get_user_manager
from api.dependencies.authentication.backend import authentication_backend

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)

current_active_user = fastapi_users.current_user(
    active=True,
)
current_active_superuser = fastapi_users.current_user(
    active=True,
    superuser=True,
)
