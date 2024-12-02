from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.match import MatchCreate, MatchUpdate, MatchResponse
from app.crud import match as crud_match
from app.utils.security import get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/matches/{match_id}", response_model=MatchResponse)
def get_match_details(match_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_match = crud_match.get_match(db=db, match_id=match_id)
    if db_match is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return db_match

@router.post("/matches", response_model=MatchResponse)
def create_match(match: MatchCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud_match.create_match(db=db, match=match)

@router.post("/matches/{match_id}/results", response_model=MatchResponse)
def update_match_results(match_id: int, match: MatchUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_match = crud_match.get_match(db=db, match_id=match_id)
    if db_match is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return crud_match.update_match_results(db=db, match_id=match_id, match=match)

@router.get("/matches", response_model=list[MatchResponse])
def get_matches(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud_match.get_matches(db=db)