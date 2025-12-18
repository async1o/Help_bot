from aiogram.filters import BaseFilter
from aiogram.types import Message

from src.db.repositories import UserRepository

class IsAdmin(BaseFilter):
    async def __call__(self, message: Message):

        user = await UserRepository().get_user_by_id(user_id=str(message.from_user.id))
        return user.is_admin
    