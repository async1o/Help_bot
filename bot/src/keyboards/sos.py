from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

all_right_message = '✅ Все верно'
cancel_message = '🚫 Отменить'

def confirmation_kb() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text=all_right_message), KeyboardButton(text=cancel_message)]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons)