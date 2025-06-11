from pydantic import BaseModel
from typing import Optional

from products.product import ProductType

class ProductShemaBase(BaseModel):
    name:str
    price:int
    amount:int
    type:ProductType

class ProductShema(ProductShemaBase):
    product_id:int


