from pydantic import BaseModel
from typing import Optional

class LeagueBase(BaseModel):
    league_name: str
    league_type: str
    max_teams: Optional[int] = 10
    draft_date: Optional[str]

class LeagueCreate(LeagueBase):
    pass

class LeagueUpdate(BaseModel):
    league_name: Optional[str]

class LeagueResponse(LeagueBase):
    leagueID: int
    commissioner: int

    class Config:
        orm_mode: True
