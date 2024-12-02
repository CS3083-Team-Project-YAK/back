from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.database import get_db
from app.routes import user

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/login")

app.include_router(user.router, prefix="/api", tags=["users"])

@app.get("/ping")
def ping_db(db: Session = Depends(get_db)):
    try:
        # Perform a simple query to check the connection
        db.execute(text("SELECT 1"))
        return {"message": "Database connection successful"}
    except Exception as e:
        return {"message": "Database connection failed", "error": str(e)}