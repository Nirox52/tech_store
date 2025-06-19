from datetime import date
from sqlalchemy.orm import Session

from orders.shema import  OrderShemaBase
from orders.orders import Order, OrderStatus


def add_order(db: Session,order:OrderShemaBase):#Create new order
    order = Order(user_id=order.user_id,product_id=order.product_id,status=order.status)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def get_order_by_order_id(db: Session, order_id: int): #Get order by order_id
    return db.query(Order).filter(Order.order_id == order_id).first()

def get_order_by_order_status(db: Session, order_status: OrderStatus): #Get all orders with order_status
    return db.query(Order).filter(Order.status == order_status).all()

def get_orders_by_date_range_for_user(db:Session,user_id:int,start_date:date,end_date:date):
    return db.query(Order)\
            .filter(Order.user_id==user_id)\
            .filter(Order.created_at>=start_date)\
            .filter(Order.created_at<=end_date)\
            .all()

def get_orders_by_date_range(db:Session,start_date:date,end_date:date):
    return db.query(Order)\
            .filter(Order.created_at>=start_date)\
            .filter(Order.created_at<=end_date)\
            .all()

def get_order_by_user_id(db: Session, user_id: int): #Get all orders by user_id
    return db.query(Order).filter(Order.user_id == user_id).all()

def update_oreder_status(db: Session,order_id:int, order_status: OrderStatus): #Update order status by order_id
    db.query(Order).filter(Order.order_id == order_id).update({'status':order_status})
    db.commit()
    return get_order_by_order_id(db,order_id) 
    # return db.query(Order).where(Order.order_id == order_id).value(Order.status == order_status)

def delete_order_by_order_id(db: Session, order_id: int): #Delete order by order_id
    order = db.query(Order).filter(Order.order_id == order_id).first()
    if order:
        db.delete(order)
        db.commit()
        return True
    return False

