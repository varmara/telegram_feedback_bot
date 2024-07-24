import logging

from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message
from fluent.runtime import FluentLocalization
from pydantic import SecretStr

logger = logging.getLogger(__name__)

router = Router()

@router.message(Command(commands=["help"]))
async def help_command(
    message: Message,
    bot: Bot,
    l10n: FluentLocalization,
    admin_chat_id: SecretStr,
    admin_topic_id: int,
) -> None:
    logger.debug("Help command handler called from admin chat.")
    
    await bot.send_message(
        chat_id=admin_chat_id.get_secret_value(),
        message_thread_id=admin_topic_id,
        text=l10n.format_value("help-text-admin"),
        parse_mode="HTML",
    )
    logger.info("Help command response sent to admin chat.")
