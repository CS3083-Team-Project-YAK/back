from sqlalchemy import Column, String, Integer, Float, ForeignKey, Date, Text
from app.database import Base

class Player(Base):
    __tablename__ = "player"

    playerID = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(50), nullable=False)
    sport = Column(String(3), nullable=False)
    position = Column(String(3))
    teamID = Column(Integer, ForeignKey("team.teamID"))
    real_team = Column(String(50))
    fantasy_points = Column(Float, default=0.00)
    availability_status = Column(String(1))

class PlayerStatistics(Base):
    __tablename__ = "player_statistics"

    statisticsID = Column(Integer, primary_key=True, index=True)
    playerID = Column(Integer, ForeignKey("player.playerID"))
    match_date = Column(Date)
    performance_stats = Column(Text)
    injury_status = Column(String(1))