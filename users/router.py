from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from auth.router import validate_auth_user
from auth.utils import WORKERS_DICT, check_if_user_is_worker
from users.crud import *
from database import SessionLocal
from users.schema import UserSchemaBase, UserShema

router = APIRouter(prefix="/users",tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/",tags=["Users"]) #Get all users
def get_all(user:UserSchemaBase = Depends(validate_auth_user),db: Session = Depends(get_db)):
    check_if_user_is_worker(user)
    return get_all_users(db)

@router.get("/{user_id}",tags=["Users"]) #Get user by user_id
def get_user(user_id: int,user:UserSchemaBase = Depends(validate_auth_user), db: Session = Depends(get_db)):
    return get_user_by_user_id(db, user_id)

@router.delete("/{user_id}",tags=["Users"]) #Delete user by user_id
def delete_user(user_id: int,user:UserShema = Depends(validate_auth_user), db: Session = Depends(get_db)):
    if user.role in WORKERS_DICT or user.user_id == user_id:
        return delete_user_by_user_id(db, user_id)
    else:
        raise HTTPException(status.HTTP_403_FORBIDDEN)

