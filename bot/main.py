import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommandScopeAllPrivateChats, BotCommandScopeChat
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.default import DefaultBotProperties

from src.utils.config import settings
from src.handlers import main_router
from src.utils.argparser import add_args
from src.utils.commands_menu import get_keyboard_for_menu

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    session = AiohttpSession()

    await add_args()

    bot = Bot(
        token=settings.TOKEN,
        session=session,
        default=DefaultBotProperties(parse_mode='HTML')
    )

    dp = Dispatcher()
    dp.include_router(main_router)

    #await bot.set_my_commands(commands=get_keyboard_for_menu(), scope=BotCommandScopeAllPrivateChats())

    try:
        await dp.start_polling(bot)
    except ValueError as e:
        logger.error('ValueError occured: %s: ', e)
    except KeyError as e:
        logger.error("KeyError occured: %s: ", e)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())