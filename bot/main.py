import logging
import asyncio
import argparse

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.default import DefaultBotProperties

from src.utils.config import settings
from src.db.db import reset_tables, create_tables
from src.handlers import main_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    session = AiohttpSession()
    parser = argparse.ArgumentParser()

    parser.add_argument('--create_tables', action='store_true')
    parser.add_argument('--reset_tables', action='store_true')

    args = parser.parse_args()

    if args.create_tables:
        await create_tables()

    if args.reset_tables:
        await reset_tables()

    bot = Bot(
        token=settings.TOKEN,
        session=session,
        default=DefaultBotProperties(parse_mode='HTML')
    )

    dp = Dispatcher()
    dp.include_router(main_router)
    
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