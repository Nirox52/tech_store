from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Users(Base): #Users model
    __tablename__="users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    email:Mapped[str]
    password: Mapped[str]
    role:Mapped[str]

