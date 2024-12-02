from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import date

class LeagueBase(BaseModel):
    league_name: str
    league_type: str
    max_teams: Optional[int] = 10
    draft_date: Optional[str]

    @field_validator('draft_date', mode='before')
    def format_draft_date(cls, v):
        if isinstance(v, date):
            return v.isoformat()
        return v

class LeagueCreate(LeagueBase):
    draft_date: Optional[str] = None

class LeagueUpdate(BaseModel):
    league_name: Optional[str]
    league_type: Optional[str]
    max_teams: Optional[int]
    draft_date: Optional[str]

    @field_validator('draft_date', mode='before')
    def format_draft_date(cls, v):
        if isinstance(v, date):
            return v.isoformat()
        return v

class LeagueResponse(LeagueBase):
    leagueID: int
    commissioner: int

    class Config:
        orm_mode: True