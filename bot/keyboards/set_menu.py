from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeDefault
from fluent.runtime import FluentLocalization
from pydantic import SecretStr


async def set_bot_commands(
    bot: Bot, l10n: FluentLocalization, admin_chat_id: SecretStr
) -> None:
    user_commands = [
        BotCommand(
            command="/help",
            description=l10n.format_value("command-help-description-user"),
        ),
    ]
    await bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())

    admin_commands = [
        BotCommand(
            command="/help",
            description=l10n.format_value("command-help-description-admin"),
        ),
    ]
    await bot.set_my_commands(
        admin_commands,
        scope=BotCommandScopeChat(
            chat_id=admin_chat_id.get_secret_value()
        ),
    )
