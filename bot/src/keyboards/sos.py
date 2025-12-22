from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

all_right_message = '✅ Все верно'
cancel_message = '🚫 Отменить'

def confirmation_kb() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text=all_right_message), KeyboardButton(text=cancel_message)]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons)

def operator_request_kb() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='✅ Принять', callback_data='start_diolog')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)