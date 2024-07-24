import logging

from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message
from fluent.runtime import FluentLocalization
logger = logging.getLogger(__name__)

router = Router()


@router.message(Command(commands=["help"]))
async def help_command(message: Message, bot: Bot, l10n: FluentLocalization) -> None:
    logger.debug("Help command handler called from user pm.")

    await message.reply(l10n.format_value("help-text-user"))

    logger.info("Help command response sent to user.")
