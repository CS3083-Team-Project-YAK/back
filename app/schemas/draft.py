from pydantic import BaseModel
from typing import Optional

class DraftBase(BaseModel):
    leagueID: int
    draft_date: Optional[str]
    draft_order: Optional[str]
    draft_status: Optional[str]

class DraftCreate(DraftBase):
    pass

class DraftUpdate(BaseModel):
    draft_status: Optional[str]

class DraftResponse(DraftBase):
    draftID: int

    class Config:
        orm_mode: True
