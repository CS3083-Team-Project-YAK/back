from sqlalchemy import Column, String, Integer, Text
from app.database import Base

class User(Base):
    __tablename__ = "user"

    userID = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(50))
    username = Column(String(20), unique=True, index=True)
    email_address = Column(String(50), unique=True, index=True)
    password = Column(String(64))
    profile_setting = Column(Text)
