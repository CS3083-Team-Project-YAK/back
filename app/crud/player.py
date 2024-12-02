from sqlalchemy.orm import Session
from app.models.player import Player, PlayerStatistics
from app.models.team import Team
from app.models.league import League
from app.schemas.player import PlayerCreate, PlayerUpdate

def get_available_players(db: Session, league_id: int, status: str):
    return db.query(Player).join(Team).filter(Team.leagueID == league_id, Player.availability_status == status).all()

def add_player_to_team(db: Session, team_id: int, player_id: int):
    db_player = db.query(Player).filter(Player.playerID == player_id).first()
    if db_player:
        db_player.teamID = team_id
        db_player.availability_status = 'U'  # Update status to unavailable
        db.commit()
        db.refresh(db_player)
    return db_player

def remove_player_from_team(db: Session, team_id: int, player_id: int):
    db_player = db.query(Player).filter(Player.playerID == player_id, Player.teamID == team_id).first()
    if db_player:
        db_player.teamID = None
        db_player.availability_status = 'A'  # Update status to available
        db.commit()
        db.refresh(db_player)
    return db_player

def get_players_by_team(db: Session, team_id: int):
    return db.query(Player).filter(Player.teamID == team_id).all()

def get_league(db: Session, league_id: int):
    return db.query(League).filter(League.leagueID == league_id).first()

def create_player(db: Session, player: PlayerCreate):
    db_player = Player(**player.dict())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def update_player(db: Session, player_id: int, player: PlayerUpdate):
    db_player = db.query(Player).filter(Player.playerID == player_id).first()
    if db_player:
        for key, value in player.dict(exclude_unset=True).items():
            setattr(db_player, key, value)
        db.commit()
        db.refresh(db_player)
    return db_player

def get_player(db: Session, player_id: int):
    return db.query(Player).filter(Player.playerID == player_id).first()

def get_player_statistics(db: Session, player_id: int):
    return db.query(PlayerStatistics).filter(PlayerStatistics.playerID == player_id).all()