import enum
from sqlalchemy import ForeignKey,DateTime,func
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class OrderStatus(enum.Enum):
    Unconfirmed = 'unconfirmed'
    Confirmed = 'confirmed'
    Done = 'done'
    Paid = 'paid'

class Order(Base): # Order model
    __tablename__="orders"

    order_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id"))
    # status:Mapped[str]
    status:Mapped[OrderStatus] = mapped_column(default=OrderStatus.Unconfirmed)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
