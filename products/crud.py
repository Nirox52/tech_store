from sqlalchemy.orm import Session
from products.product import Products

def add_product(db: Session,name:str,price:int,amount:int,type:str): #Create new product
    product = Products(name=name,price=price,amount=amount,type=type)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_product_by_product_id(db: Session, product_id: int): #Get product by product_id
    return db.query(Products).filter(Products.product_id == product_id).first()

def delete_product_by_product_id(db: Session, product_id: int): #Delete product by product_id
    product = db.query(Products).filter(Products.product_id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
        return True
    return False

