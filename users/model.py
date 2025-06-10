from sqlalchemy.orm import Mapped, mapped_column
from database import Base
import enum

class Role(enum.Enum):
    ADMIN = "admin"
    SELLER = "seller"
    CONSULTANT = 'consultant'
    CUSTOMER = "customer"


class Users(Base): #Users model
    __tablename__="users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    email:Mapped[str] = mapped_column(unique=True)
    password: Mapped[bytes]
    role:Mapped[Role] = mapped_column(default=Role.ADMIN)

