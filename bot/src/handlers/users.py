from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from src.db.repository import UserRepository
from src.schemas.users import UserSchema
from src.states.sos_states import SosStates
from src.keyboards.sos import confirmation_kb, cancel_message, all_right_message

router = Router()

@router.message(F.text == '/start')
async def start(message: Message, state: FSMContext):
    user_schema = UserSchema(user_id=str(message.from_user.id),
                             full_name=message.from_user.full_name,
                             is_operator=False,
                             is_admin=False)
    
    await UserRepository().add_user(user_schema)
    await message.answer(text=f'Здравствуйте {message.from_user.full_name}\nПодробно опишите вашу проблему')
    await state.set_state(SosStates.confirmation)

@router.message(F.text == '/id')
async def get_id(message: Message):
    await message.answer(text=str(message.from_user.id))

@router.message(SosStates.confirmation)
async def confirm_request(message: Message, state: FSMContext):
    await state.update_data(sumbit=message.text)

    await message.answer(text='Убедитесь, что всё правильно', reply_markup=confirmation_kb())

    await state.set_state(SosStates.sumbit)
    
@router.message(lambda message: message.text not in [cancel_message, all_right_message], SosStates.sumbit)
async def incorrect_answer(message: Message):
    await message.answer(text='Такого варианта не было')

@router.message(F.text == cancel_message, SosStates.sumbit)
async def cancel_answer(message: Message, state: FSMContext):

    await message.answer(text='Отменено!', reply_markup=ReplyKeyboardRemove())

    await state.clear()

@router.message(F.text == all_right_message, SosStates.sumbit)
async def apply_answer(message: Message, state: FSMContext):
    try:
        ...

        await message.answer(text='Запрос отправлен!', reply_markup=ReplyKeyboardRemove())

    except:
        await message.answer(text='Что-то пошло не так', reply_markup=ReplyKeyboardRemove())

    finally:
        await state.clear()


