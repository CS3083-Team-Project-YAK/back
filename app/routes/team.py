from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.team import TeamCreate, TeamUpdate, TeamResponse
from app.crud import team as crud_team
from app.crud import league as crud_league
from app.utils.security import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/teams/", response_model=TeamResponse)
def create_team(team: TeamCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_league = crud_team.get_league(db=db, league_id=team.leagueID)
    if db_league is None:
        raise HTTPException(status_code=404, detail="League not found")
    if db_league.league_type == 'R' and db_league.commissioner != current_user.userID:
        raise HTTPException(status_code=403, detail="Not authorized to create a team in this private league")
    return crud_team.create_team(db=db, team=team, owner_id=current_user.userID)

@router.get("/teams/", response_model=list[TeamResponse])
def read_teams(league_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_league = crud_team.get_league(db=db, league_id=league_id)
    if db_league is None:
        raise HTTPException(status_code=404, detail="League not found")
    if db_league.league_type == 'R' and db_league.commissioner != current_user.userID:
        raise HTTPException(status_code=403, detail="Not authorized to view teams in this private league")
    return crud_team.get_teams_by_league(db=db, league_id=league_id)

@router.put("/teams/{team_id}", response_model=TeamResponse)
def update_team(team_id: int, team: TeamUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_team = crud_team.get_team(db=db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    db_league = crud_team.get_league(db=db, league_id=db_team.leagueID)
    if db_league.league_type == 'R' and db_league.commissioner != current_user.userID:
        raise HTTPException(status_code=403, detail="Not authorized to update a team in this private league")
    if db_team.owner != current_user.userID:
        raise HTTPException(status_code=403, detail="Not authorized to update this team")
    return crud_team.update_team(db=db, team_id=team_id, team=team)

@router.delete("/teams/{team_id}", response_model=dict)
def delete_team(team_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_team = crud_team.get_team(db=db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    db_league = crud_team.get_league(db=db, league_id=db_team.leagueID)
    if db_league.league_type == 'R' and db_league.commissioner != current_user.userID:
        raise HTTPException(status_code=403, detail="Not authorized to delete a team in this private league")
    if db_team.owner != current_user.userID:
        raise HTTPException(status_code=403, detail="Not authorized to delete this team")
    crud_team.delete_team(db=db, team_id=team_id)
    return {"message": "Team deleted successfully"}

@router.post("/teams/{league_id}/update-rankings", response_model=dict)
def update_team_rankings(league_id: int, db: Session = Depends(get_db)):
    db_league = crud_league.get_league(db=db, league_id=league_id)
    if db_league is None:
        raise HTTPException(status_code=404, detail="League not found")
    # if db_league.commissioner != current_user.userID:
    #     raise HTTPException(status_code=403, detail="Not authorized to update team rankings in this league")
    crud_team.update_team_rankings(db=db, league_id=league_id)
    return {"message": "Team rankings updated successfully"}