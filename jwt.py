from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from database import SessionLocal
from utils import create_access_token, hash_password, verify_password, decode_acess_token
from pydantic import BaseModel
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models import User


router = APIRouter()
security = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
class UserCreate(BaseModel):
    username: str
    password: str 
    
@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = hash_password(user.password)
    new_user = User(username=user.username,hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"username": new_user.username, "id": new_user.id}

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail = "Invalid Credentials")
    create_access = create_access_token({"sub": db_user.username})
    return {"access_token": create_access, "token_type":"bearer", "user": db_user}    