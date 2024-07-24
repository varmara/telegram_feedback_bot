import logging

from aiogram import Bot, Router, exceptions
from aiogram.types import Message
from fluent.runtime import FluentLocalization
from pydantic import SecretStr

from bot.utils.functions import admin_time

logger = logging.getLogger(__name__)

router = Router()


@router.message()
async def echo_handler(
    message: Message,
    bot: Bot,
    l10n: FluentLocalization,
    admin_chat_id: SecretStr,
    admin_topic_id: int,
) -> None:
    logger.debug("Message handler called.")
    try:
        user_id = getattr(message.from_user, "id", None)
        user_full_name = getattr(message.from_user, "full_name", "Unknown")
        username = getattr(message.from_user, "username", " unknown_username")
        formatted_message = message.html_text
        logger.info(
            f"User {user_id} ({user_full_name}, @{username}): New message. Chat id {admin_chat_id}. Topic id {admin_topic_id}. Message: {formatted_message}"
        )

        MSG_FROM = f"<a href='tg://user?id={user_id}'>{user_full_name}</a> (@{username}) {admin_time()}\n\n{formatted_message}"

        await bot.send_message(
            chat_id=admin_chat_id.get_secret_value(),
            message_thread_id=admin_topic_id,
            text=MSG_FROM,
            parse_mode="HTML",
        )

        logger.debug("Message sent.")
        await message.reply(l10n.format_value("thank-you-message-accepted"))
    except exceptions.TelegramAPIError as e:
        logger.exception("An error occurred:")  # Log the full traceback
        if "message thread not found" in str(e).lower():
            logger.exception("Thread not found:")
        await message.answer(l10n.format_value("error-send-message"))
    except TypeError:
        await message.answer(l10n.format_value("error-unsupported-message-type"))
