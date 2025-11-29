import logging

from sqlalchemy import insert, select

from src.db.db import async_session_maker
from src.models.users import UserModel
from src.schemas.users import UserSchema

logger = logging.getLogger('Repositories')

class UserRepository:

    async def get_user_by_id(self, user_id: str):
        async with async_session_maker() as session:

            stmt = select(UserModel).where(UserModel.user_id == user_id)
            res = (await session.execute(stmt)).fetchall()
            logger.info(msg='User handled from DB')

            return res

    async def add_user(self, user: UserSchema):
        async with async_session_maker() as session:

            if await self.get_user_by_id(user.user_id):
                return
            
            
            stmt = insert(UserModel).values(user.model_dump())
            logger.info(msg='User added to DB')
            
            await session.execute(stmt)
            await session.commit()
