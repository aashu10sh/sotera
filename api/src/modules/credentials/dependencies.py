from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.dependencies.get_db import get_db
from src.modules.credentials.infra.repositories.credential_repository import (
    CredentialRepository,
)


def get_credential_repository(
    db: AsyncSession = Depends(get_db),
) -> CredentialRepository:
    return CredentialRepository(db=db)
