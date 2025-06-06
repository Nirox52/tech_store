from pydantic import BaseModel
from typing import Optional

class OrderShemaBase(BaseModel):
    order_id:int
    user_id:int
    status:str

class OrderShema(OrderShemaBase):
    order_id:int

