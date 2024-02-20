from src.core.domain.repositories.repository_interface import RepositoryInterface
from src.modules.auth.domain.entities.session_request_entity import SessionRequestEntity


class SessionRepositoryInterface(RepositoryInterface[SessionRequestEntity]):
    pass
