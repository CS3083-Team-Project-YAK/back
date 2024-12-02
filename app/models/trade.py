from sqlalchemy import Column, Integer, Date, ForeignKey
from app.database import Base

class Trade(Base):
    __tablename__ = "trade"

    tradeID = Column(Integer, primary_key=True, index=True)
    trade_date = Column(Date)
    team1ID = Column(Integer, ForeignKey("team.teamID"))
    team2ID = Column(Integer, ForeignKey("team.teamID"))
    player1ID = Column(Integer, ForeignKey("player.playerID"))
    player2ID = Column(Integer, ForeignKey("player.playerID"))
