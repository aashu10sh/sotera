from sqlalchemy.ext.asyncio import AsyncSession
from src.core.infra.repositories.repository import Repository
from src.core.models.sessions import SessionModel
from src.modules.auth.domain.entities.session_request_entity import SessionRequestEntity
from src.modules.auth.domain.repositories.session_repository_interface import (
    SessionRepositoryInterface,
)


class SessionRepository(
    Repository[SessionModel, SessionRequestEntity], SessionRepositoryInterface
):
    def __init__(
        self,
        db: AsyncSession,
    ) -> None:
        super().__init__(db, SessionModel, SessionRequestEntity)
