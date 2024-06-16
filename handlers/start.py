import logging
from textwrap import dedent

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from utils.functions import moscow_time

logger = logging.getLogger(__name__)

router = Router() 

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Handler receives messages with `/start` command
    """
    user_id = getattr(message.from_user, "id", None)  # Get id or None if not present
    user_full_name = getattr(message.from_user, "full_name", "Unknown")  # Get full_name or "Unknown"
    username = getattr(message.from_user, "username", "unknown_username")  # Get username or "unknown_username"

    MSG_HELLO = dedent(f"""\
        Здравствуйте, {user_full_name}!
        Это бот для сбора предложений для канала. 
        Напишите сообщение, и оно будет переправлено редакторам.
        """)
    logging.info(f"{moscow_time()} {user_id=} {user_full_name=} {username=}: Started bot.")
    await message.answer(MSG_HELLO)

