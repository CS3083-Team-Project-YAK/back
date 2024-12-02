from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from app.database import get_db
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.crud import user as crud_user
from app.utils.security import create_access_token, verify_password, get_current_user
from app.models.user import User  # Import the User model

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/login")

@router.post("/users/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    from app.crud.user import get_user_by_username  # Local import to avoid circular dependency
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    new_user = crud_user.create_user(db=db, user=user)
    return new_user  # Return the new user object

@router.post("/users/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    from app.crud.user import get_user_by_username  # Local import to avoid circular dependency
    db_user = get_user_by_username(db, username=form_data.username)
    if not db_user or not verify_password(form_data.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": db_user.username})
    return {"token": access_token, "token_type": "bearer", "user_id": db_user.userID}

@router.get("/users/profile", response_model=UserResponse, dependencies=[Depends(oauth2_scheme)])
def read_user_profile(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/users/settings", response_model=UserResponse, dependencies=[Depends(oauth2_scheme)])
def update_user_settings(user: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_user = crud_user.update_user(db, user_id=current_user.userID, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user  # Return the updated user object