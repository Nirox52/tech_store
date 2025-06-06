from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from products.crud import *
from database import SessionLocal

router = APIRouter(prefix="/products",tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/",tags=["Products"]) #Create product
def create_product(name:str,price:int,amount:int,type:str,db:Session=Depends(get_db)):
    return add_product(db,name,price,amount,type)

@router.get("/{product_id}",tags=["Products"]) #Get product by product_id
def get_product(product_id: int, db: Session = Depends(get_db)):
    return get_product_by_product_id(db, product_id)

@router.delete("/{product_id}",tags=["Products"]) #Delete product by product_id
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return delete_product_by_product_id(db, product_id)

