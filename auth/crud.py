from sqlalchemy.orm import Session
# from users.schema import *
from users.model import Users
from users.schema import UserShemaCreate

def add_user(db: Session,created_user:UserShemaCreate): #Create new user
    user = Users(email=created_user.email,password=created_user.password,role=created_user.role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str): #Get user by user_id
    return db.query(Users).filter(Users.email == email).first()
