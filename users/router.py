from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from users.crud import *
from database import SessionLocal

router = APIRouter(prefix="/users",tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/",tags=["Users"]) #Create new user
def create_user(email:str,password:str,role: str, db: Session = Depends(get_db)):
    return add_user(db,email,password, role)

@router.get("/{user_id}",tags=["Users"]) #Get user by user_id
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_user_id(db, user_id)

@router.delete("/{user_id}",tags=["Users"]) #Delete user by user_id
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user_by_user_id(db, user_id)

