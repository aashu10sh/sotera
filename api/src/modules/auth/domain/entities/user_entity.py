from typing import Optional
from pydantic import BaseModel, ConfigDict


class UserEntity(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    nonce: Optional[str] = None
    key_id : Optional[int] = None
    key: Optional[str] = None
    username: Optional[str] = None
