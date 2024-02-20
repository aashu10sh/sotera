from src.core.domain.repositories.user_repository_interface import (
    UserRepositoryInterface,
)
from src.modules.auth.domain.entities.user_entity import UserEntity
from src.modules.auth.domain.utils.auth.generate_username import generate_username
from src.modules.auth.domain.utils.auth.genereate_key import generate_random_key


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    async def execute(self, key_id: int, nonce: str) -> UserEntity:
        created = await self.user_repository.create(
            obj=UserEntity(
                key_id=key_id,
                nonce=nonce,
                key=generate_random_key(),
                username=generate_username(),
            )
        )
        if not created:
            raise ValueError
        return created
