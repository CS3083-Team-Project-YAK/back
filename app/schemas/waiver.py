from pydantic import BaseModel
from typing import Optional

class WaiverBase(BaseModel):
    teamID: int
    playerID: int
    waiver_order: Optional[int]
    waiver_status: Optional[str]
    pickup_date: Optional[str]

class WaiverCreate(WaiverBase):
    pass

class WaiverUpdate(BaseModel):
    waiver_status: Optional[str]

class WaiverResponse(WaiverBase):
    waiverID: int

    class Config:
        orm_mode: True
