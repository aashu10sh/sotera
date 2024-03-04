from src.core.domain.repositories.repository_interface import RepositoryInterface
from src.modules.credentials.domain.entities.credential_entity import CredentialEntity


class CredentialRepositoryInterface(RepositoryInterface[CredentialEntity]):
    pass
