from pydantic import BaseModel


class CreateCredentialRequest(BaseModel):
    website: str
    password: str
