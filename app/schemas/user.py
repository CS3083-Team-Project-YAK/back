from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    full_name: Optional[str]
    username: str
    email_address: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    full_name: Optional[str]
    profile_setting: Optional[str]

class UserResponse(UserBase):
    userID: int

    class Config:
        orm_mode: True
