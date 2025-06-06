from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from orders.crud import *
from database import SessionLocal

router = APIRouter(prefix="/orders",tags=["Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/",tags=["Orders"])
def create_order(user_id:int,product_id:int,status:str,db:Session=Depends(get_db)):
    return add_order(db,user_id,product_id,status)

@router.get("/{order_id}",tags=["Orders"])
def get_user(order_id: int, db: Session = Depends(get_db)):
    return get_order_by_order_id(db, order_id)

@router.delete("/{order_id}",tags=["Orders"])
def delete_user(order_id: int, db: Session = Depends(get_db)):
    return delete_order_by_order_id(db, order_id)


