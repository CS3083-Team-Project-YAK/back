from sqlalchemy.orm import Session
from app.models.match import Match
from app.schemas.match import MatchCreate, MatchUpdate

def get_match(db: Session, match_id: int):
    return db.query(Match).filter(Match.matchID == match_id).first()

def create_match(db: Session, match: MatchCreate):
    db_match = Match(**match.model_dump())
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match

def update_match_results(db: Session, match_id: int, match: MatchUpdate):
    db_match = db.query(Match).filter(Match.matchID == match_id).first()
    if db_match:
        for key, value in match.model_dump(exclude_unset=True).items():
            setattr(db_match, key, value)
        db.commit()
        db.refresh(db_match)
    return db_match

def get_matches(db: Session):
    return db.query(Match).all()