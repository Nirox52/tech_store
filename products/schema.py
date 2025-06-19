from pydantic import BaseModel
from datetime import datetime

from products.product import ProductType

class ProductShemaCreate(BaseModel):
    name:str
    price:float
    amount:int
    type:ProductType

class ProductShemaBase(ProductShemaCreate):
    created_at:datetime

class ProductShema(ProductShemaBase):
    product_id:int


