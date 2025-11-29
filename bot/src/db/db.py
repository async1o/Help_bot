import logging

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from src.utils.config import settings

logger = logging.getLogger('Database')

engine = create_async_engine(
    url = settings.get_url_db,
)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def reset_tables():
    async with engine.begin() as eng:
        await eng.run_sync(Base.metadata.drop_all)
        await eng.run_sync(Base.metadata.create_all)
        logger.info('Tables reset')
    

async def create_tables():
    async with engine.begin() as eng:
        await eng.run_sync(Base.metadata.create_all)
        logger.info('Tables created')
    