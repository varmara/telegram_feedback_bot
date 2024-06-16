import logging
from textwrap import dedent

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from utils.functions import moscow_time

logger = logging.getLogger(__name__)

router = Router()

@router.message(Command("help"))  # Triggered by the "/help" command
async def help_command(message: Message) -> None:
    help_text = dedent("""\
        /start - начать работу
        /help - показать помощь
        """)
    await message.answer(help_text)