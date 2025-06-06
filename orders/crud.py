from sqlalchemy.orm import Session
from .orders import Order

def add_order(db: Session,user_id:int,product_id:int,status:str): #Create new order
    order = Order(user_id=user_id,product_id=product_id,status=status)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def get_order_by_order_id(db: Session, order_id: int): #Get order by order_id
    return db.query(Order).filter(Order.order_id == order_id).first()

def delete_order_by_order_id(db: Session, order_id: int): #Delete order by order_id
    order = db.query(Order).filter(Order.order_id == order_id).first()
    if order:
        db.delete(order)
        db.commit()
        return True
    return False

