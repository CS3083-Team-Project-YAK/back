from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Team(Base):
    __tablename__ = "team"

    teamID = Column(Integer, primary_key=True, index=True)
    leagueID = Column(Integer, ForeignKey("league.leagueID"))
    owner = Column(Integer, ForeignKey("user.userID"))
    total_points = Column(Float, default=0.00)
    ranking = Column(Integer)
    status = Column(String(1))

    league_rel = relationship("League")
    owner_rel = relationship("User")
