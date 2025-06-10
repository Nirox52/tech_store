from datetime import datetime,date
from pydantic import BaseModel

from orders.orders import OrderStatus

class OrderShemaCreate(BaseModel):
    product_id:int
    # status:str
    created_at:datetime

class OrderShemaBase(OrderShemaCreate):
    user_id:int 
    status:OrderStatus


class OrderShema(OrderShemaBase):
    order_id:int

