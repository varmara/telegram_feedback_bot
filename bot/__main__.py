import asyncio
import logging
import logging.config
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from dotenv import load_dotenv
from fluent.runtime import FluentLocalization

from bot.config.config import Settings, get_settings
from bot.handlers import attach_routers_and_middlewares
from bot.keyboards.set_menu import set_bot_commands
from bot.locales.locale_loader import get_fluent_localization
from bot.logging.logging import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


async def main():
    # Setup config
    logger.debug("Setting up config.")
    load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")
    config: Settings = get_settings()

    # Setup localization
    logger.debug("Setting up localization.")
    l10n: FluentLocalization = get_fluent_localization(config.bot.language)

    # Setup storage
    logger.debug("Setting up storage.")
    storage = RedisStorage.from_url(config.redis.dsn)

    # Setup bot
    logger.debug("Starting bot.")
    bot = Bot(token=config.bot.token.get_secret_value())
    dp = Dispatcher(
        storage=storage,
        # bot=bot,
        l10n=l10n,
        admin_chat_id=config.bot.admin_chat_id,
        admin_topic_id=config.bot.admin_topic_id,
        config_bot=config.bot,
    )

    # Register routers and middlewares
    logger.debug("Setting up routers and middlewares.")
    attach_routers_and_middlewares(dispatcher=dp)

    # Register bot commands
    logger.debug("Setting up bot commands.")
    await set_bot_commands(bot, l10n=l10n, admin_chat_id=config.bot.admin_chat_id)

    logger.debug("Starting polling.")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
