from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.database import get_db
from app.routes import user, league, team, player, match

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],   
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/login")

app.include_router(user.router, prefix="/api", tags=["users"])
app.include_router(league.router, prefix="/api", tags=["leagues"])
app.include_router(team.router, prefix="/api", tags=["teams"])
app.include_router(player.router, prefix="/api", tags=["players"])
app.include_router(match.router, prefix="/api", tags=["matches"])



@app.get("/ping")
def ping_db(db: Session = Depends(get_db)):
    try:
        # Perform a simple query to check the connection
        db.execute(text("SELECT 1"))
        return {"message": "Database connection successful"}
    except Exception as e:
        return {"message": "Database connection failed", "error": str(e)}