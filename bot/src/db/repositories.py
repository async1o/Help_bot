import logging
from typing import List

from sqlalchemy import insert, select, update

from src.db.db import async_session_maker
from src.models.users import UserModel
from src.schemas.users import UserSchema
from src.utils.config import settings

logger = logging.getLogger('Repositories')

class UserRepository:
    async def get_user_by_id(self, user_id: str):
        async with async_session_maker() as session:

            stmt = select(UserModel).where(UserModel.user_id == user_id)
            res = (await session.execute(stmt)).scalar()
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
    
class AdminRepository:
    async def add_start_admins(self):
        for admin_id in settings.ADMINS.split(','):
            await UserRepository().add_user(
                UserSchema(
                    user_id=admin_id,
                    is_admin=True,
                    is_operator=False
                )
            )
        logger.info(msg='Admins added to DB')
    
    async def get_admins(self):
        async with async_session_maker() as session:


            stmt = select(UserModel.user_id).where(UserModel.is_admin == True)

            res = await session.execute(stmt)

            return res.all()
        
    async def get_operators(self):
        async with async_session_maker() as session:


            stmt = select(UserModel).where(UserModel.is_operator == True)

            res = await session.execute(stmt)

            return res.all()

    async def update_roles(self, user_id: str, add: bool, operator: bool):
        async with async_session_maker() as session:
            
            if not await UserRepository().get_user_by_id(user_id):
                raise NotImplementedError
            
            role = 'is_operator' if operator else 'is_admin'

            stmt = update(UserModel).where(UserModel.user_id == user_id).values({role: add})
            await session.execute(stmt)
            await session.commit()

    async def get_all_operators(self):
        async with async_session_maker() as session:
            stmt = select(UserModel.user_id).where(UserModel.is_operator == True)
            res = (await session.execute(stmt)).all()
            return res


