from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class League(Base):
    __tablename__ = "league"

    leagueID = Column(Integer, primary_key=True, index=True)
    commissioner = Column(Integer, ForeignKey("user.userID"))
    league_name = Column(String(30), nullable=False)
    league_type = Column(String(1), nullable=False)
    max_teams = Column(Integer, default=10)
    draft_date = Column(Date)

    commissioner_rel = relationship("User")
