from src.modules.credentials.domain.entities.credential_entity import CredentialEntity
from src.modules.credentials.domain.repositories.credential_repository_interface import (
    CredentialRepositoryInterface,
)


class ValidateCorrectUserUseCase:
    def __init__(self, credential_repository: CredentialRepositoryInterface) -> None:
        self.credential_repository: CredentialRepositoryInterface = (
            credential_repository
        )

    async def execute(self, credential_id: int, user_id: int) -> bool:
        credential: CredentialEntity | None = await self.credential_repository.find_one(
            obj=CredentialEntity(id=credential_id)
        )
        if not credential:
            raise Exception

        return credential.user_id == user_id
