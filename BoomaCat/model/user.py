from datetime import datetime

from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    username: str
    password: str
    name: str
    is_admin: bool
    created_at: datetime