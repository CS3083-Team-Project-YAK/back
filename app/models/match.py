from sqlalchemy import Column, String, Integer, Date, ForeignKey
from app.database import Base

class Match(Base):
    __tablename__ = "matches"

    matchID = Column(Integer, primary_key=True, index=True)
    team1ID = Column(Integer, ForeignKey("team.teamID"))
    team2ID = Column(Integer, ForeignKey("team.teamID"))
    winner = Column(Integer, ForeignKey("team.teamID"))
    match_date = Column(Date)
    final_score = Column(String(10))
