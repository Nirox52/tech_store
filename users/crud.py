from sqlalchemy.orm import Session
# from users.schema import *
from users.model import Users

def add_user(db: Session,email:str,password:str,role: str): #Create new user
    user = Users(email=email,password=password,role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_user_id(db: Session, user_id: int): #Get user by user_id
    return db.query(Users).filter(Users.user_id == user_id).first()

def delete_user_by_user_id(db: Session, user_id: int): #Delete user by user_id
    user = db.query(Users).filter(Users.user_id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

