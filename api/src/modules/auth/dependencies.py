from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.dependencies.get_db import get_db
from src.core.infra.repositories.user_repository import UserRepository
from src.modules.auth.infra.repositories.session_repository import SessionRepository


def get_user_repository(db: AsyncSession = Depends(get_db)) -> UserRepository:
    return UserRepository(db=db)


def get_session_repository(db: AsyncSession = Depends(get_db)) -> SessionRepository:
    return SessionRepository(db=db)
