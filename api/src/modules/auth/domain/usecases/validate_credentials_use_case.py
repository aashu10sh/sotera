from src.core.domain.repositories.user_repository_interface import (
    UserRepositoryInterface,
)
from src.modules.auth.domain.entities.user_entity import UserEntity


class ValidateCredentialsUseCase:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    async def execute(self, key_id: int, nonce: str) -> UserEntity | None:
        entity = await self.user_repository.find_one(
            obj=UserEntity(key_id=key_id, nonce=nonce)
        )
        return entity
