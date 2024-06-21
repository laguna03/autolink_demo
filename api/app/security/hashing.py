from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import Depends
from app.services.postgre_connector import connect_to_database
from app.models.classes.user_table import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(email: str, password: str, db: Session = Depends(connect_to_database)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user