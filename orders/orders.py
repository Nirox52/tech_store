from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Order(Base): # Order model
    __tablename__="orders"

    order_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id"))
    status:Mapped[str]
