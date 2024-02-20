from pydantic import BaseModel, ConfigDict


class UserRequest(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    key_id: int
    nonce: str
