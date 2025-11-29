__all__ = ['main_router',]

from aiogram import Router

from .users import router as users_router

main_router = Router()

main_router.include_routers(users_router)