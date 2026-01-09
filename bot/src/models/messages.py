from typing import Union

from sqlalchemy.orm import Mapped, mapped_column

from src.db.db import Base

class MsgModel(Base):
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    message_id: Mapped[int] = mapped_column(unique=True)
    text: Mapped[str]
    operator_id: Mapped[str]
    sender_id: Mapped[str]