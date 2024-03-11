from fastapi import Depends, Request
from src.core.domain.repositories.user_repository_interface import (
    UserRepositoryInterface,
)
from src.core.exc.error_codes import ErrorCode
from src.core.exc.sotera_exception import SoteraException
from src.modules.auth.dependencies import get_session_repository, get_user_repository
from src.modules.auth.domain.entities.session_request_entity import SessionRequestEntity

from src.modules.auth.domain.entities.user_entity import UserEntity
from src.modules.auth.domain.repositories.session_repository_interface import (
    SessionRepositoryInterface,
)
from datetime import datetime


async def get_current_user(
    request: Request,
    session_repository: SessionRepositoryInterface = Depends(get_session_repository),
    user_repository: UserRepositoryInterface = Depends(get_user_repository),
) -> UserEntity:
    access_token: str | None = request.headers.get("Authorization")
    if not access_token:
        raise SoteraException(
            status_code=403,
            code=ErrorCode.INSUFFICIENT_PERMISSION,
            msg="No Token",
        )
    print(access_token)
    access_token = access_token.split(" ")[-1]
    session: SessionRequestEntity | None = await session_repository.find_one(
        obj=SessionRequestEntity(key=access_token)
    )
    if not session:
        raise SoteraException(
            status_code=401,
            code=ErrorCode.NOT_FOUND,
            msg="A Session Like that does not exist",
        )
    if datetime.now() > session.expires_at:  # type:ignore
        raise SoteraException(
            status_code=401,
            code=ErrorCode.TOKEN_EXPIRED,
            msg="Your Token is Expied, Please Relogin",
        )

    user: UserEntity | None = await user_repository.find_one(
        obj=UserEntity(id=session.user_id)
    )
    if not user:
        raise SoteraException(
            status_code=500, code=ErrorCode.UNKOWN_ERROR, msg="Something Went Wrong!"
        )

    return user
