import logging
from fastapi import Depends
from src.core.domain.repositories.user_repository_interface import (
    UserRepositoryInterface,
)
from src.core.exc.error_codes import ErrorCode
from src.core.exc.sotera_exception import SoteraException
from src.modules.auth.dependencies import get_session_repository, get_user_repository
from src.modules.auth.domain.entities.session_entity import SessionEntity
from src.modules.auth.domain.entities.user_entity import UserEntity
from src.modules.auth.domain.entities.user_request import UserRequest
from src.modules.auth.domain.repositories.session_repository_interface import (
    SessionRepositoryInterface,
)
from src.modules.auth.domain.usecases.create_user_use_case import CreateUserUseCase
from src.modules.auth.domain.usecases.generate_session_use_case import (
    GenerateSessionUseCase,
)
from src.modules.auth.domain.usecases.validate_credentials_use_case import (
    ValidateCredentialsUseCase,
)


class AuthController:
    @classmethod
    async def create(
        cls,
        user_request: UserRequest,
        user_repository: UserRepositoryInterface = Depends(get_user_repository),
        session_repository: SessionRepositoryInterface = Depends(
            get_session_repository
        ),
    ) -> SessionEntity:
        create_user_use_case = CreateUserUseCase(user_repository=user_repository)
        created: UserEntity | None = None
        try:
            created = await create_user_use_case.execute(
                user_request.key_id, user_request.nonce
            )
        except ValueError:
            raise SoteraException(
                status_code=409,
                code=ErrorCode.DUPLICATE_ENTRY,
                msg="Account with that Credential Already Exists",
            )
        generate_session_use_case = GenerateSessionUseCase(
            session_repository=session_repository
        )

        try:
            session_generated = await generate_session_use_case.execute(
                user_id=created.id  # type:ignore
            )
        except ValueError:
            raise SoteraException(
                status_code=500,
                code=ErrorCode.NOT_FOUND,
                msg="Could not generate Session Key!",
            )
        logging.info(f"Created {created}")
        return SessionEntity(key=session_generated.key)

    @classmethod
    async def login(
        cls,
        user_request: UserRequest,
        user_repository: UserRepositoryInterface = Depends(get_user_repository),
        session_repository: SessionRepositoryInterface = Depends(
            get_session_repository
        ),
    ) -> SessionEntity:
        validate_credentials = ValidateCredentialsUseCase(
            user_repository=user_repository
        )
        validated = await validate_credentials.execute(
            key_id=user_request.key_id, nonce=user_request.nonce
        )
        if not validated:
            raise SoteraException(
                status_code=403,
                code=ErrorCode.INVALID_FIELDS,
                msg="Incorrect Credentials",
            )
        generate_session = GenerateSessionUseCase(session_repository=session_repository)
        session = await generate_session.execute(validated.id)  # type:ignore
        return SessionEntity(key=session.key)
