from sqlalchemy.orm import Session
from sqlalchemy import text
from app.models.team import Team
from app.models.league import League
from app.schemas.team import TeamCreate, TeamUpdate

def get_team(db: Session, team_id: int):
    return db.query(Team).filter(Team.teamID == team_id).first()

def get_teams_by_league(db: Session, league_id: int):
    return db.query(Team).filter(Team.leagueID == league_id).all()

def get_all_teams(db: Session):
    return db.query(Team).all()

def create_team(db: Session, team: TeamCreate, owner_id: int):
    db_team = Team(leagueID=team.leagueID, owner=owner_id)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    db.execute(text("CALL UpdateTeamRankings(:league_id);"), {'league_id': team.leagueID})
    db.commit()
    return db_team

def update_team(db: Session, team_id: int, team: TeamUpdate):
    db_team = db.query(Team).filter(Team.teamID == team_id).first()
    if db_team:
        for key, value in team.model_dump(exclude_unset=True).items():
            setattr(db_team, key, value)
        db.commit()
        db.refresh(db_team)
    return db_team

def delete_team(db: Session, team_id: int):
    db_team = db.query(Team).filter(Team.teamID == team_id).first()
    if db_team:
        db.delete(db_team)
        db.commit()
    return db_team

def get_league_by_team(db: Session, team_id: int):
    db_team = db.query(Team).filter(Team.teamID == team_id).first()
    if db_team:
        return db.query(League).filter(League.leagueID == db_team.leagueID).first()
    return None

def update_team_rankings(db: Session, league_id: int):
    db.execute(text("CALL UpdateTeamRankings(:league_id);"), {'league_id': league_id})
    db.commit()