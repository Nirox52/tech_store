from pydantic import BaseModel
from typing import Optional

class ProductShemaBase(BaseModel):
    name:str
    price:int
    amount:int
    type:str

class ProductShema(ProductShemaBase):
    product_id:int


