from typing import Optional
from pydantic import BaseModel, ConfigDict


class CredentialEntity(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int] = None
    user_id: Optional[int] = None
    website: Optional[str] = None
    password: Optional[str] = None
