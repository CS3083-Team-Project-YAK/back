from pydantic import BaseModel
from typing import Optional

class PlayerBase(BaseModel):
    full_name: str
    sport: str
    position: Optional[str]
    teamID: Optional[int]
    real_team: Optional[str]
    fantasy_points: Optional[float] = 0.00
    availability_status: Optional[str]

class PlayerCreate(PlayerBase):
    pass

class PlayerUpdate(BaseModel):
    teamID: Optional[int]
    availability_status: Optional[str]

class PlayerResponse(PlayerBase):
    playerID: int

    class Config:
        orm_mode: True
