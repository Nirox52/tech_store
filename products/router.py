from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from auth.router import validate_auth_user
from auth.utils import check_if_user_is_worker
from products.crud import *
from database import SessionLocal
from products.schema import ProductShemaBase
from users.model import Role
from users.schema import  UserSchemaBase, UserShemaAuth

router = APIRouter(prefix="/products",tags=["Products"])

http_bearer = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/",tags=["Products"],response_model=ProductShemaBase) #Create product
def create_product(product:ProductShemaBase,
                   user:UserSchemaBase=Depends(validate_auth_user),
                   db:Session=Depends(get_db)):
    check_if_user_is_worker(user)
    return add_product(db,product.name,product.price,product.amount,product.type)

@router.get("/{product_id}",tags=["Products"]) #Get product by product_id
def get_product(product_id: int,
                user:UserSchemaBase = Depends(validate_auth_user), 
                db: Session = Depends(get_db)):
    check_if_user_is_worker(user)
    return get_product_by_product_id(db, product_id)

@router.delete("/{product_id}",tags=["Products"]) #Delete product by product_id
def delete_product(product_id: int,
                   user:UserSchemaBase = Depends(validate_auth_user), 
                   db: Session = Depends(get_db)):
    check_if_user_is_worker(user)
    return delete_product_by_product_id(db, product_id)

