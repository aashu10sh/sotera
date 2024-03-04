from typing import List
from src.modules.credentials.domain.entities.credential_entity import CredentialEntity
from src.modules.credentials.domain.repositories.credential_repository_interface import (
    CredentialRepositoryInterface,
)


class GetCredentialsUseCase:
    def __init__(self, credential_repository: CredentialRepositoryInterface) -> None:
        self.credential_repository = credential_repository

    async def execute(
        self, page: int, limit: int, sort_by: str, order: str, user_id: int
    ) -> List[CredentialEntity]:
        offset = (page - 1) * limit
        descending: bool = order == "desc"
        credentials = await self.credential_repository.find_many(
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            descending=descending,
            filter=CredentialEntity(user_id=user_id),
        )
        return credentials
