from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.player import PlayerCreate, PlayerUpdate, PlayerResponse
from app.crud import player as crud_player
from app.utils.security import get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/players/", response_model=list[PlayerResponse])
def get_available_players(league_id: int, status: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Get available players in a league.
    - **league_id**: ID of the league
    - **status**: Availability status of the players (e.g., 'available')
    """
    db_league = crud_player.get_league(db=db, league_id=league_id)
    if db_league is None:
        raise HTTPException(status_code=404, detail="League not found")
    if db_league.league_type == 'R' and db_league.commissioner != current_user.userID:
        raise HTTPException(status_code=403, detail="Not authorized to view players in this private league")
    return crud_player.get_available_players(db=db, league_id=league_id, status=status)

@router.post("/teams/{team_id}/players", response_model=dict)
def add_player_to_team(team_id: int, player_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Add a player to a team.
    - **team_id**: ID of the team
    - **player_id**: ID of the player to be added
    """
    db_team = crud_player.get_team(db=db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    db_league = crud_player.get_league(db=db, league_id=db_team.leagueID)
    if db_league.league_type == 'R' and db_league.commissioner != current_user.userID:
        raise HTTPException(status_code=403, detail="Not authorized to add players to this private league")
    if db_team.owner != current_user.userID:
        raise HTTPException(status_code=403, detail="Not authorized to add players to this team")
    crud_player.add_player_to_team(db=db, team_id=team_id, player_id=player_id)
    return {"message": "Player added to team successfully"}

@router.delete("/teams/{team_id}/players/{player_id}", response_model=dict)
def remove_player_from_team(team_id: int, player_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Remove a player from a team.
    - **team_id**: ID of the team
    - **player_id**: ID of the player to be removed
    """
    db_team = crud_player.get_team(db=db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    db_league = crud_player.get_league(db=db, league_id=db_team.leagueID)
    if db_league.league_type == 'R' and db_league.commissioner != current_user.userID:
        raise HTTPException(status_code=403, detail="Not authorized to remove players from this private league")
    if db_team.owner != current_user.userID:
        raise HTTPException(status_code=403, detail="Not authorized to remove players from this team")
    crud_player.remove_player_from_team(db=db, team_id=team_id, player_id=player_id)
    return {"message": "Player removed from team successfully"}

@router.get("/teams/{team_id}/players", response_model=list[PlayerResponse])
def get_players_by_team(team_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Get all players in a team.
    - **team_id**: ID of the team
    """
    db_team = crud_player.get_team(db=db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    db_league = crud_player.get_league(db=db, league_id=db_team.leagueID)
    if db_league.league_type == 'R' and db_league.commissioner != current_user.userID:
        raise HTTPException(status_code=403, detail="Not authorized to view players in this private league")
    return crud_player.get_players_by_team(db=db, team_id=team_id)

@router.post("/players/", response_model=PlayerResponse)
def create_player(player: PlayerCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Create a new player.
    - **player**: PlayerCreate schema containing player details
    """
    db_league = crud_player.get_league(db=db, league_id=player.leagueID)
    if db_league is None:
        raise HTTPException(status_code=404, detail="League not found")
    if db_league.commissioner != current_user.userID:
        raise HTTPException(status_code=403, detail="Not authorized to add players to this league")
    return crud_player.create_player(db=db, player=player)

@router.put("/players/{player_id}", response_model=PlayerResponse)
def update_player(player_id: int, player: PlayerUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Update a player's details.
    - **player_id**: ID of the player to be updated
    - **player**: PlayerUpdate schema containing updated player details
    """
    db_player = crud_player.get_player(db=db, player_id=player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    db_league = crud_player.get_league(db=db, league_id=db_player.teamID)
    if db_league is None:
        raise HTTPException(status_code=404, detail="League not found")
    if db_league.league_type == 'R' and db_league.commissioner != current_user.userID:
        raise HTTPException(status_code=403, detail="Not authorized to update players in this private league")
    if db_player.teamID and db_player.team.owner != current_user.userID and db_league.commissioner != current_user.userID:
        raise HTTPException(status_code=403, detail="Not authorized to update this player")
    if db_league.commissioner == current_user.userID:
        # Commissioner can update any field
        return crud_player.update_player(db=db, player_id=player_id, player=player)
    if db_player.team.owner == current_user.userID:
        # Owner can only update availability_status
        if 'availability_status' in player.dict(exclude_unset=True):
            return crud_player.update_player(db=db, player_id=player_id, player=PlayerUpdate(availability_status=player.availability_status))
        else:
            raise HTTPException(status_code=403, detail="Not authorized to update fields other than availability_status")
    raise HTTPException(status_code=403, detail="Not authorized to update this player")