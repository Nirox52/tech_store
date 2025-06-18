from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from auth.utils import check_if_user_is_worker
from orders.crud import *
from database import SessionLocal
from orders.orders import OrderStatus
from orders.shema import  OrderShemaBase, OrderShemaCreate
from products.crud import subtract_product
from users.schema import UserSchemaBase, UserShema
from auth.router import validate_auth_user

router = APIRouter(prefix="/orders",tags=["Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/",tags=["Orders"],response_model=OrderShemaBase)
def create_order(order:OrderShemaCreate,
                 user:UserShema = Depends(validate_auth_user), 
                 db:Session=Depends(get_db)):
    subtract_product(db,order.product_id)
    order_to_create = OrderShemaBase(
                    product_id=order.product_id,
                    status=OrderStatus.Unconfirmed,
                    user_id=user.user_id,
                    created_at=order.created_at)
    return add_order(db,order_to_create)

@router.get("/{order_id}",tags=["Orders"])
def get_order_by_id(order_id: int,
                    user:UserSchemaBase = Depends(validate_auth_user), 
                    db: Session = Depends(get_db)):
    check_if_user_is_worker(user)
    return get_order_by_order_id(db, order_id)

@router.get("/user/date/",tags=["Orders"])
def get_order_by_date_range_for_user(start_date:date,
                                     end_date:date,
                                     user:UserShema= Depends(validate_auth_user), 
                                     db: Session = Depends(get_db)):
    return get_orders_by_date_range_for_user(db,user.user_id,start_date,end_date) 

@router.get("/date/",tags=["Orders"])
def get_order_by_date_range(start_date:date,
                            end_date:date,
                            user:UserSchemaBase= Depends(validate_auth_user), 
                            db: Session = Depends(get_db)):
    check_if_user_is_worker(user)
    return get_orders_by_date_range(db,start_date,end_date) 

@router.get("/status/{order_status}",tags=["Orders"])
def get_order_by_status(order_status: OrderStatus,
                        user:UserSchemaBase= Depends(validate_auth_user), 
                        db: Session = Depends(get_db)):
    check_if_user_is_worker(user)
    return get_order_by_order_status(db, order_status)

@router.get("/my/",tags=["Orders"])
def get_my_orders(user:UserShema= Depends(validate_auth_user), 
                  db: Session = Depends(get_db)):
    return get_order_by_user_id(db,user.user_id)

@router.patch("/pay/{order_id}",tags=["Orders"])
def pay_order(order_id: int, 
              user:UserShema= Depends(validate_auth_user), 
              db: Session = Depends(get_db)):
    order = get_order_by_order_id(db,order_id)
    if order: #Check if order is exist
        if order.user_id != user.user_id: #Check if user_id = user_id in the order
            raise HTTPException(status.HTTP_403_FORBIDDEN,detail='Wrong order tried to pay')
        if order.status == OrderStatus.Unconfirmed: #Check if order status is not unconfirmed
            raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE,'Your order hasn\'t confirmed yet')
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)
    return update_oreder_status(db,order_id,OrderStatus.Paid)

@router.patch("/status/{order_id}",tags=["Orders"],response_model=OrderShemaBase)
def update_status(order_id:int,
                  order_status:OrderStatus = OrderStatus.Confirmed,
                  user:UserSchemaBase = Depends(validate_auth_user),
                  db:Session = Depends(get_db)):
    check_if_user_is_worker(user)
    return update_oreder_status(db,order_id,order_status)

@router.delete("/{order_id}",tags=["Orders"])
def delete_order(order_id: int,
                 user:UserSchemaBase = Depends(validate_auth_user), 
                 db: Session = Depends(get_db)):
    check_if_user_is_worker(user)
    return delete_order_by_order_id(db, order_id)


