from pydantic import BaseModel
from typing import Optional

class TeamBase(BaseModel):
    leagueID: int
    owner: int
    total_points: Optional[float] = 0.00
    ranking: Optional[int]
    status: Optional[str]

class TeamCreate(BaseModel):
    leagueID: int

class TeamUpdate(BaseModel):
    status: Optional[str]

class TeamResponse(TeamBase):
    teamID: int

    class Config:
        orm_mode: True