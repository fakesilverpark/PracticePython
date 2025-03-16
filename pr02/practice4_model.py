from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class RoleEnum(str, Enum):
    ASSASSIN = "암살자"
    FIGHTER = "전사"
    MARKSMAN = "원거리"
    MAGE = "마법사"
    TANK = "탱커"
    SUPPORT = "서포터"

class Champion(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=12)
    release_date: datetime
    role: RoleEnum