

from api.src.modules.auth.domain.entities.session_entity import SessionEntity
from src.modules.auth.domain.entities.user_request import UserRequest


class UserController:
    @classmethod
    async def create(cls, user_request : UserRequest )-> SessionEntity:
        