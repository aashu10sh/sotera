from src.core.domain.repositories.repository_interface import RepositoryInterface
from src.modules.auth.domain.entities.user_entity import UserEntity


class UserRepositoryInterface(RepositoryInterface[UserEntity]):
    pass
