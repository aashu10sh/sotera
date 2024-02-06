from typing import Optional
from pydantic import BaseModel


class SessionEntity(BaseModel):
    # id : Optional[int] = None 
    # user_id : Optional[int] = 
    key : Optional[str]
    