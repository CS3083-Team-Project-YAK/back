from pydantic import BaseModel
from typing import Optional

class EventBase(BaseModel):
    matchID: int
    event_type: Optional[str]
    event_time: Optional[str]
    impact_on_points: Optional[float] = 0.00

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    impact_on_points: Optional[float]

class EventResponse(EventBase):
    eventID: int

    class Config:
        orm_mode: True
