from fastapi import Depends
from src.core.dependencies.get_current_user import get_current_user
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
