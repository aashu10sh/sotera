from typing import List
from fastapi import Depends
from src.core.dependencies.get_current_user import get_current_user
from src.core.exc.error_codes import ErrorCode
from src.core.exc.sotera_exception import SoteraException
from src.modules.auth.domain.entities.user_entity import UserEntity
from src.modules.credentials.dependencies import get_credential_repository
from src.modules.credentials.domain.entities.create_credential import (
    CreateCredentialRequest,
)
from src.modules.credentials.domain.entities.credential_entity import CredentialEntity
from src.modules.credentials.domain.repositories.credential_repository_interface import (
    CredentialRepositoryInterface,
)
from src.modules.credentials.domain.usecases.create_credential_use_case import (
    CreateCredentialUsecase,
)
from src.modules.credentials.domain.usecases.delete_credential_use_case import (
    DeleteCredentialUseCase,
)
from src.modules.credentials.domain.usecases.get_credentials_use_case import (
    GetCredentialsUseCase,
)
from src.modules.credentials.domain.usecases.validate_correct_user_use_case import (
    ValidateCorrectUserUseCase,
)


class CredentialController:
    @classmethod
    async def store(
        cls,
        request: CreateCredentialRequest,
        user: UserEntity = Depends(get_current_user),
        credential_repository: CredentialRepositoryInterface = Depends(
            get_credential_repository
        ),
    ) -> CredentialEntity:
        create_credential_use_case = CreateCredentialUsecase(
            credential_repository=credential_repository
        )
        entity = await create_credential_use_case.execute(
            user_id=user.id,  # type:ignore
            website=request.website,
            password=request.password,
        )
        return entity

    @classmethod
    async def delete(
        cls,
        id: int,
        user: UserEntity = Depends(get_current_user),
        credential_repository: CredentialRepositoryInterface = Depends(
            get_credential_repository
        ),
    ):
        validate_correct_user_use_case = ValidateCorrectUserUseCase(
            credential_repository=credential_repository
        )
        validated = await validate_correct_user_use_case.execute(
            user_id=user.id,  # type:ignore
            credential_id=id,
        )
        if not validated:
            raise SoteraException(
                status_code=403,
                code=ErrorCode.INSUFFICIENT_PERMISSION,
                msg="You are not Authorized to Perform this Action",
            )
        delete_credential_use_case = DeleteCredentialUseCase(
            credential_repository=credential_repository
        )

        await delete_credential_use_case.execute(id=id)

    @classmethod
    async def get(
        cls,
        page: int = 1,
        limit: int = 20,
        sort_by: str = "updated_at",
        order: str = "desc",
        user: UserEntity = Depends(get_current_user),
        credential_repository: CredentialRepositoryInterface = Depends(
            get_credential_repository
        ),
    ) -> List[CredentialEntity]:
        get_credentials_use_case = GetCredentialsUseCase(
            credential_repository=credential_repository
        )
        credentials: List[CredentialEntity] = await get_credentials_use_case.execute(
            page=page,
            limit=limit,
            sort_by=sort_by,
            order=order,
            user_id=user.id,  # type:ignore
        )
        return credentials
