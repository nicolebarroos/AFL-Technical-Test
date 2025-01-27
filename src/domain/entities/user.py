from datetime import datetime
from passlib.context import CryptContext
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import validates
from src.infrastructure.database import Base
import re

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, email: str, password: str, created_at: datetime = None):
        self.email = email
        self.password = self.hash_password(password)
        self.created_at = created_at or datetime.utcnow()

    def hash_password(self, plain_password: str) -> str:
        return pwd_context.hash(plain_password)

    def verify_password(self, plain_password: str) -> bool:
        return pwd_context.verify(plain_password, self.password)
