from sqlalchemy.ext.asyncio import AsyncSession
from src.core.infra.repositories.repository import Repository
from src.core.models.credentials import CredentialModel
from src.modules.credentials.domain.entities.credential_entity import CredentialEntity
from src.modules.credentials.domain.repositories.credential_repository_interface import (
    CredentialRepositoryInterface,
)


class CredentialRepository(
    Repository[CredentialModel, CredentialEntity], CredentialRepositoryInterface
):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(db, CredentialModel, CredentialEntity)
