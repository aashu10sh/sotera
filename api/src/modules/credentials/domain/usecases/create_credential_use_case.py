from src.modules.credentials.domain.entities.credential_entity import CredentialEntity
from src.modules.credentials.domain.repositories.credential_repository_interface import (
    CredentialRepositoryInterface,
)
import random 


class CreateCredentialUsecase:
    def __init__(self, credential_repository: CredentialRepositoryInterface) -> None:
        self.credential_repository: CredentialRepositoryInterface = (
            credential_repository
        )

    async def execute(
        self, user_id: int, website: str, password: str
    ) -> CredentialEntity:
        already: CredentialEntity | None = await self.credential_repository.find_one(
            obj=CredentialEntity(website=website)
        )
        if already:
            website = website + str(random.choice(list(range(0,10)))) # generate_random_key()

        created: CredentialEntity | None = await self.credential_repository.create(
            obj=CredentialEntity(user_id=user_id, website=website, password=password)
        )
        if not created:
            raise ValueError
        return created
