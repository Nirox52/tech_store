from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func,update
from starlette.middleware import P
from products.product import ProductType, Products
from datetime import datetime, timedelta

def add_product(db: Session,name:str,price:int,amount:int,type:str): #Create new product
    product = Products(name=name,price=price,amount=amount,type=type)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_product_by_product_id(db: Session, product_id: int): #Get product by product_id
    return db.query(Products).filter(Products.product_id == product_id).first()

def get_product_by_product_tyupe(db: Session, product_type: ProductType): #Get product by product_id
    return db.query(Products).filter(Products.type == product_type).all()

def get_all_products(db: Session): #Get product by product_id
    return db.query(Products).all()

def check_all_products_with_diskount(db:Session):
    #Geting all products what were created 30 day ago
    old_objects = db.query(Products)\
        .filter(Products.created_at < datetime.utcnow() - timedelta(days=30))\
        .all()

    #Update price with diskount
    for obj in old_objects:
        obj.price = obj.price * 0.8
        print(obj.price)

    db.commit()

def subtract_product(db:Session,product_id:int):
    prod = get_product_by_product_id(db,product_id)
    print(prod)
    if prod and prod.amount>0: #Check if product is exist
        db.query(Products).filter(Products.product_id == product_id).update({Products.amount:prod.amount-1})
        db.commit()
        return get_product_by_product_id(db,product_id)
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,detail='Product does not exist')

def delete_product_by_product_id(db: Session, product_id: int): #Delete product by product_id
    product = db.query(Products).filter(Products.product_id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
        return True
    return False

