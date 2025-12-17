from aiogram.fsm.state import State, StatesGroup


class SosStates(StatesGroup):
    confirmation = State()
    sumbit = State()

