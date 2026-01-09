from aiogram import Router, F
from aiogram.types import CallbackQuery

from src.db.repositories import MsgRepository

router = Router()



@router.callback_query(F.data == 'start_diolog')
async def delete_messages(callback: CallbackQuery):
    text = callback.message.text
    messages = await MsgRepository().get_message(text=text)

    for message in messages:
        await callback.bot.delete_message(chat_id=message[0].operator_id, message_id=message[0].message_id)
    
    await MsgRepository().delete_message(text=text)

    await start_diolog(messages[0][0].sender_id, callback.from_user.id)


async def start_diolog(sender_id, operator_id):
    print(sender_id, operator_id)