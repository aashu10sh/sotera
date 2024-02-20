from sqlalchemy.ext.asyncio import AsyncSession
from src.core.domain.repositories.user_repository_interface import (
    UserRepositoryInterface,
)
from src.core.infra.repositories.repository import Repository
from src.core.models.users import UserModel
from src.modules.auth.domain.entities.user_entity import UserEntity


class UserRepository(Repository[UserModel, UserEntity], UserRepositoryInterface):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(db, UserModel, UserEntity)
