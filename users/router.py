from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from users.crud import *
from database import SessionLocal
from users.schema import UserShemaAuth, UserShemaCreate

router = APIRouter(prefix="/users",tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def validate_user():
    pass

@router.post("/",tags=["Users"]) #Create new user
# def create_user(email:str,password:str,role: str, db: Session = Depends(get_db)):
#     return add_user(db,email,password, role)
def create_user(user:UserShemaCreate = Depends(None), db: Session = Depends(get_db)):
    return add_user(db,user.email,user.password, user.role)

@router.get("/",tags=["Users"]) #Create new user
def get_all(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/{user_id}",tags=["Users"]) #Get user by user_id
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_user_id(db, user_id)

@router.delete("/{user_id}",tags=["Users"]) #Delete user by user_id
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user_by_user_id(db, user_id)

