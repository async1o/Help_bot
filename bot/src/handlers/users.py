from aiogram import Router, F
from aiogram.types import Message

from src.db.repository import UserRepository
from src.schemas.users import UserSchema

router = Router()

@router.message(F.text == '/start')
async def start(message: Message):
    user_schema = UserSchema(user_id=str(message.from_user.id), #type: ignore
                             full_name=message.from_user.full_name, #type: ignore
                             is_operator=False,
                             is_admin=False)
    
    await UserRepository().add_user(user_schema)
    await message.answer(text=f'Hello! {message.from_user.full_name}') #type: ignore

