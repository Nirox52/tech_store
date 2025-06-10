from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Products(Base): #Products model
    __tablename__="products"

    product_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[int]
    amount: Mapped[int]
    type: Mapped[str]
