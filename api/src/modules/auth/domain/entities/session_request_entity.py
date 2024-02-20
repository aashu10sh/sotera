from typing import Optional
from pydantic import ConfigDict
from .session_entity import SessionEntity
from datetime import datetime


class SessionRequestEntity(SessionEntity):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    user_id: Optional[int] = None
    key: Optional[str] = None
    expires_at: Optional[datetime] = None
