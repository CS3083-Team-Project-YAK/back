from sqlalchemy import Column, Integer, Date, ForeignKey, String
from app.database import Base

class Waiver(Base):
    __tablename__ = "waiver"

    waiverID = Column(Integer, primary_key=True, index=True)
    teamID = Column(Integer, ForeignKey("team.teamID"))
    playerID = Column(Integer, ForeignKey("player.playerID"))
    waiver_order = Column(Integer)
    waiver_status = Column(String(1))
    pickup_date = Column(Date)
