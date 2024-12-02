from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import date

class PlayerBase(BaseModel):
    full_name: str
    sport: str
    position: Optional[str]
    teamID: Optional[int]
    real_team: Optional[str]
    fantasy_points: Optional[float] = 0.00
    availability_status: Optional[str]

class PlayerCreate(PlayerBase):
    real_team: str

class PlayerUpdate(BaseModel):
    teamID: Optional[int]
    real_team: Optional[str]
    position: Optional[str]
    availability_status: Optional[str]

class PlayerResponse(PlayerBase):
    playerID: int

    class Config:
        orm_mode: True

class PlayerStatisticsResponse(BaseModel):
    statisticsID: int
    playerID: int
    match_date: str
    performance_stats: str
    injury_status: Optional[str]

    @field_validator('match_date', mode='before')
    def format_draft_date(cls, v):
        if isinstance(v, date):
            return v.isoformat()
        return v

    class Config:
        orm_mode: True