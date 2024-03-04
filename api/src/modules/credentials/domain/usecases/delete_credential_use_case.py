from src.modules.credentials.domain.entities.credential_entity import CredentialEntity
from src.modules.credentials.domain.repositories.credential_repository_interface import (
    CredentialRepositoryInterface,
)


class DeleteCredentialUseCase:
    def __init__(self, credential_repository: CredentialRepositoryInterface) -> None:
        self.credential_repository = credential_repository

    async def execute(self, id: int) -> None:
        await self.credential_repository.delete(conditions=CredentialEntity(id=id))
