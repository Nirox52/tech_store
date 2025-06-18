import enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime,func
from database import Base
from datetime import datetime

class ProductType(enum.Enum):
    Phone = 'phone'
    Laptop = 'laptop'
    Household= 'household'
    Other = 'other'

class Products(Base): #Products model
    __tablename__="products"

    product_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[float]
    amount: Mapped[int]
    type: Mapped[ProductType]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
