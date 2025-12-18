from typing import Annotated
from fastapi import (
    APIRouter,
    Depends,
)

from application.core.schemas.user import UserRead
from core.models import User
from core.config import settings
from .fastapi_users import (
    current_active_user,
    current_active_superuser,
)

router = APIRouter(
    prefix=settings.api.v1.messages,
    tags=["Messages"],
)


@router.get("")
def get_user_messages(
    user: Annotated[
        User,
        Depends(current_active_user),
    ],
):
    return {
        "messsages": [
            "m1",
            "m2",
            "m3",
        ],
        "user": UserRead.model_validate(user),
    }


@router.get("/secrets")
def get_superuser_messages(
    user: Annotated[
        User,
        Depends(current_active_superuser),
    ],
):
    return {
        "messsages": [
            "secret-m1",
            "secret-m2",
            "secret-m3",
        ],
        "user": UserRead.model_validate(user),
    }
