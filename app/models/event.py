from sqlalchemy import Column, String, Integer, Time, Float, ForeignKey
from app.database import Base

class Event(Base):
    __tablename__ = "event"

    eventID = Column(Integer, primary_key=True, index=True)
    matchID = Column(Integer, ForeignKey("matches.matchID"))
    event_type = Column(String(3))
    event_time = Column(Time)
    impact_on_points = Column(Float, default=0.00)
