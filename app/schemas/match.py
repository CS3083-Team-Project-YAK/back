from pydantic import BaseModel
from typing import Optional

class MatchBase(BaseModel):
    team1ID: int
    team2ID: int
    winner: Optional[int]
    match_date: str
    final_score: Optional[str]

class MatchCreate(MatchBase):
    pass

class MatchUpdate(BaseModel):
    winner: Optional[int]
    final_score: Optional[str]

class MatchResponse(MatchBase):
    matchID: int

    class Config:
        orm_mode: True
