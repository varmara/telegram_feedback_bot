import logging

from aiogram import Dispatcher, F, Router
from aiogram.enums.chat_type import ChatType

from bot.handlers.admin_chat import admin_commands
from bot.handlers.user import user_commands, user_message, user_start
from bot.middlewares.userinfo import UserInfoMiddleware

logger = logging.getLogger(__name__)


def attach_routers_and_middlewares(dispatcher: Dispatcher) -> None:

    # Common routers
    # ...

    # User routers
    user_pm_router = Router(name="user_pm")
    user_pm_router.message.filter(F.chat.type == ChatType.PRIVATE)
    user_pm_router.include_router(user_start.router)
    user_pm_router.include_router(user_commands.router)
    user_pm_router.include_router(user_message.router)

    user_pm_router.message.middleware(UserInfoMiddleware())

    dispatcher.include_router(user_pm_router)
    logger.debug("User routers and middlewares attached.")

    # Admin routers
    admin_router = Router(name="admin")
    admin_router.message.filter(
        F.chat.id == int(dispatcher.workflow_data["admin_chat_id"].get_secret_value()),
        F.message_thread_id == (dispatcher.workflow_data["admin_topic_id"])
    )
    admin_router.include_router(admin_commands.router)

    dispatcher.include_router(admin_router)
    logger.debug("Admin routers and middlewares attached.")
