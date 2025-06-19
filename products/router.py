from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from auth.router import validate_auth_user
from auth.utils import check_if_user_is_worker
from products.crud import *
from database import SessionLocal
from products.product import ProductType
from products.schema import ProductShemaBase, ProductShemaCreate
from users.schema import  UserSchemaBase

router = APIRouter(prefix="/products",tags=["Products"])

http_bearer = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/",tags=["Products"],response_model=ProductShemaBase) #Create product
def create_product(product:ProductShemaCreate,
                   user:UserSchemaBase=Depends(validate_auth_user),
                   db:Session=Depends(get_db)):
    check_if_user_is_worker(user)
    return add_product(db,product.name,product.price,product.amount,product.type)

@router.get("/",tags=["Products"]) #Get all products
def get_products(user:UserSchemaBase=Depends(validate_auth_user),
                 db:Session=Depends(get_db)):
    check_if_user_is_worker(user)
    check_all_products_with_diskount(db)
    return get_all_products(db)

@router.get("/{product_id}",tags=["Products"]) #Get product by product_id
def get_product(product_id: int,
                user:UserSchemaBase = Depends(validate_auth_user), 
                db: Session = Depends(get_db)):
    check_if_user_is_worker(user)
    check_all_products_with_diskount(db)
    return get_product_by_product_id(db, product_id)

@router.get("/type/",tags=["Products"]) #Get product by product_type
def get_product_by_type(product_type: ProductType,
                user:UserSchemaBase = Depends(validate_auth_user), 
                db: Session = Depends(get_db)):
    check_all_products_with_diskount(db)
    return get_product_by_product_tyupe(db, product_type)

@router.delete("/{product_id}",tags=["Products"]) #Delete product by product_id
def delete_product(product_id: int,
                   user:UserSchemaBase = Depends(validate_auth_user), 
                   db: Session = Depends(get_db)):
    check_if_user_is_worker(user)
    return delete_product_by_product_id(db, product_id)

