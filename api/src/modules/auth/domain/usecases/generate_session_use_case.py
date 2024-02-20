from src.modules.auth.domain.entities.session_request_entity import SessionRequestEntity
from src.modules.auth.domain.repositories.session_repository_interface import (
    SessionRepositoryInterface,
)
from src.modules.auth.domain.utils.auth.generate_session_key import generate_session_key
from datetime import datetime, timedelta


class GenerateSessionUseCase:
    def __init__(self, session_repository: SessionRepositoryInterface) -> None:
        self.session_repository = session_repository

    async def execute(self, user_id: int) -> SessionRequestEntity:
        created = await self.session_repository.create(
            obj=SessionRequestEntity(
                user_id=user_id,
                key=str(
                    generate_session_key(),
                ),
                expires_at=(datetime.now() + timedelta(minutes=20)),
            )
        )
        if not created:
            raise ValueError
        return created
