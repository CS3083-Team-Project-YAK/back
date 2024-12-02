from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import date

class MatchBase(BaseModel):
    team1ID: int
    team2ID: int
    winner: Optional[int]
    match_date: str
    final_score: Optional[str]
    
    @field_validator('match_date', mode='before')
    def format_draft_date(cls, v):
        if isinstance(v, date):
            return v.isoformat()
        return v

class MatchCreate(MatchBase):
    pass

class MatchUpdate(BaseModel):
    winner: Optional[int]
    final_score: Optional[str]
    match_date: Optional[str]
    
    @field_validator('match_date', mode='before')
    def format_draft_date(cls, v):
        if isinstance(v, date):
            return v.isoformat()
        return v

class MatchResponse(MatchBase):
    matchID: int

    class Config:
        orm_mode: True