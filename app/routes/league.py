from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.league import LeagueCreate, LeagueUpdate, LeagueResponse
from app.crud import league as crud_league
from app.utils.security import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/leagues/", response_model=LeagueResponse)
def create_league(league: LeagueCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud_league.create_league(db=db, league=league, commissioner_id=current_user.userID)

@router.get("/leagues/", response_model=list[LeagueResponse])
def read_leagues(league_type: str = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if league_type == 'R':
        return crud_league.get_leagues_by_commissioner(db=db, commissioner_id=current_user.userID)
    return crud_league.get_leagues(db=db, league_type=league_type)

@router.put("/leagues/{league_id}", response_model=LeagueResponse)
def update_league(league_id: int, league: LeagueUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_league = crud_league.get_league(db=db, league_id=league_id)
    if db_league is None:
        raise HTTPException(status_code=404, detail="League not found")
    if db_league.commissioner != current_user.userID:
        raise HTTPException(status_code=403, detail="Not authorized to update this league")
    return crud_league.update_league(db=db, league_id=league_id, league=league)

@router.delete("/leagues/{league_id}", response_model=LeagueResponse)
def delete_league(league_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_league = crud_league.get_league(db=db, league_id=league_id)
    if db_league is None:
        raise HTTPException(status_code=404, detail="League not found")
    if db_league.commissioner != current_user.userID:
        raise HTTPException(status_code=403, detail="Not authorized to delete this league")
    return crud_league.delete_league(db=db, league_id=league_id)