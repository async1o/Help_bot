from aiogram import Bot
from aiogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardMarkup

from src.db.repositories import AdminRepository, MsgRepository
from src.schemas.messages import MsgSchema
from src.keyboards.sos import operator_request_kb

async def send_message_to_operator(bot: Bot, user_id: str, text: str, sender_id: int , keyboard: ReplyKeyboardMarkup | InlineKeyboardMarkup | None = None):
    message = await bot.send_message(chat_id=user_id, text=text, reply_markup=keyboard)
    await MsgRepository().add_message(MsgSchema(message_id=message.message_id,
                                                text=text,
                                                operator_id=user_id,
                                                sender_id=str(sender_id)))

async def choose_operator(bot: Bot | None, request: dict, sender_id: int):
    operators = await AdminRepository().get_all_operators()

    text = f'Новый запрос:\n{request.get("sumbit")}'
    keyboard = operator_request_kb()

    for operator in operators:
        await send_message_to_operator(bot=bot, user_id=operator[0], text=text, keyboard=keyboard, sender_id=sender_id)
