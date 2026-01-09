__all__ = ['messages_router',]

from aiogram import Router

from .users import router as users_router
from .admin import router as admin_router

messages_router = Router()

messages_router.include_routers(users_router, admin_router)