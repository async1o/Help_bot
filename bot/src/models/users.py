from typing import Union

from sqlalchemy.orm import Mapped, mapped_column

from src.db.db import Base

class UserModel(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(unique=True)
    full_name: Mapped[Union[str, None]] = mapped_column(default=None)
    is_operator: Mapped[bool] = mapped_column(default=False)
    is_admin: Mapped[bool]  = mapped_column(default=False)
