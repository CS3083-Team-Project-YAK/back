from sqlalchemy import Column, String, Integer, Date, ForeignKey
from app.database import Base

class Draft(Base):
    __tablename__ = "draft"

    draftID = Column(Integer, primary_key=True, index=True)
    leagueID = Column(Integer, ForeignKey("league.leagueID"))
    draft_date = Column(Date)
    draft_order = Column(String(1))
    draft_status = Column(String(1))
