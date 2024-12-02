from sqlalchemy.orm import Session
from app.models.league import League
from app.schemas.league import LeagueCreate, LeagueUpdate

def get_league(db: Session, league_id: int):
    return db.query(League).filter(League.leagueID == league_id).first()

def get_leagues(db: Session, league_type: str = None):
    if league_type:
        return db.query(League).filter(League.league_type == league_type).all()
    return db.query(League).all()

def get_leagues_by_commissioner(db: Session, commissioner_id: int):
    return db.query(League).filter(League.commissioner == commissioner_id).all()

def get_league_by_commissioner(db: Session, commissioner_id: int):
    return db.query(League).filter(League.commissioner == commissioner_id).first()

def create_league(db: Session, league: LeagueCreate, commissioner_id: int):
    db_league = League(**league.model_dump(), commissioner=commissioner_id)
    db.add(db_league)
    db.commit()
    db.refresh(db_league)
    return db_league

def update_league(db: Session, league_id: int, league: LeagueUpdate):
    db_league = db.query(League).filter(League.leagueID == league_id).first()
    if db_league:
        for key, value in league.model_dump(exclude_unset=True).items():
            setattr(db_league, key, value)
        db.commit()
        db.refresh(db_league)
    return db_league

def delete_league(db: Session, league_id: int):
    db_league = db.query(League).filter(League.leagueID == league_id).first()
    if db_league:
        db.delete(db_league)
        db.commit()
    return db_league