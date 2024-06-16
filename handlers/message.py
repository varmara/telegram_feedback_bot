import logging

from aiogram import Router
from aiogram import Bot
from aiogram import exceptions
from aiogram.types import Message
from aiogram.utils.text_decorations import html_decoration

from filters.forward import ForwardToFilter
from utils.functions import moscow_time

logger = logging.getLogger(__name__)

router = Router()

# @router.message(ForwardToFilter())
# async def echo_handler(message: Message, bot: Bot, chat_id: str, topic_id: int) -> None: 
#     """
#     Handler will forward a message back to the sender
#     """
#     try:
#         user_id = getattr(message.from_user, "id", None)  # Get id or None if not present
#         user_full_name = getattr(message.from_user, "full_name", "Unknown")  # Get full_name or "Unknown"
#         username = getattr(message.from_user, "username", " unknown_username")  # Get username or "unknown_username"

#         logging.info(f"{moscow_time()} User {user_id} ({user_full_name}, @{username}): New message.")

#         MSG_FROM = f"<a href='tg://user?id={user_id}'>{user_full_name}</a> (@{username})\n{moscow_time()}"

#         await bot.send_message(chat_id=chat_id, message_thread_id=topic_id, text=MSG_FROM, parse_mode="HTML")

#         await message.send_copy(chat_id=chat_id, message_thread_id=topic_id)
#         await message.answer("Спасибо! Ваше сообщение принято.")
#     except exceptions.TelegramAPIError as e:
#         logging.exception("An error occurred:") # Log the full traceback
#         if "message thread not found" in str(e).lower():
#             await message.answer("Ошибка: тема не найдена.")
#         else:
#             await message.answer("Ошибка при отправке сообщения.")
#     except TypeError:
#         await message.answer("Ошибка. Тип сообщения не поддерживается")

@router.message(ForwardToFilter())
async def echo_handler(message: Message, bot: Bot, chat_id: str, topic_id: int) -> None: 
    """
    Handler will forward a message back to the sender
    """
    try:
        user_id = getattr(message.from_user, "id", None)  # Get id or None if not present
        user_full_name = getattr(message.from_user, "full_name", "Unknown")  # Get full_name or "Unknown"
        username = getattr(message.from_user, "username", " unknown_username")  # Get username or "unknown_username"
        formatted_message = message.html_text
        logging.info(f"{moscow_time()} User {user_id} ({user_full_name}, @{username}): New message.")

        MSG_FROM = f"<a href='tg://user?id={user_id}'>{user_full_name}</a> (@{username}) {moscow_time()}\n\n{formatted_message}"

        await bot.send_message(chat_id=chat_id, message_thread_id=topic_id, text=MSG_FROM, parse_mode="HTML")

        await message.answer("Спасибо! Ваше сообщение принято.")
    except exceptions.TelegramAPIError as e:
        logging.exception("An error occurred:") # Log the full traceback
        if "message thread not found" in str(e).lower():
            await message.answer("Ошибка: тема не найдена.")
        else:
            await message.answer("Ошибка при отправке сообщения.")
    except TypeError:
        await message.answer("Ошибка. Тип сообщения не поддерживается")