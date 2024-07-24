import logging
from datetime import datetime

from aiogram import Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message
from fluent.runtime import FluentLocalization

from bot.states.states import UserState

logger = logging.getLogger(__name__)

router = Router()

# Handler outside FSM
@router.message(CommandStart(), StateFilter(default_state))
async def command_start_handler(message: Message, state: FSMContext, l10n: FluentLocalization) -> None:

    logger.debug("Start command handler (default) called. Outside FSM.")

    await message.answer(
        l10n.format_value("start-text", {"user_full_name": getattr(message.from_user, "full_name", "Unknown")})
    )
    logger.debug("Start message sent.")
    
    await state.update_data(last_activity=datetime.now().isoformat())
    logger.debug(f"Updated last activity for user {message.from_user.id}.")
    
    await state.set_state(UserState.ACTIVE) 
    current_state = await state.get_state()
    logger.debug(f"Set state for user{message.from_user.id}: {current_state}")

@router.message(CommandStart(), ~StateFilter(default_state))
async def command_start_active_user_handler(message: Message, state: FSMContext, l10n: FluentLocalization) -> None:

    logger.debug("Start command handler (active user) called.")

    user_data = await state.get_data()
    last_activity_str = user_data.get("last_activity")
    if last_activity_str:
        last_activity = datetime.fromisoformat(last_activity_str).strftime("%Y-%m-%d %H:%M:%S")
    current_state = await state.get_state() # Get the current state
    logger.debug(f"User {message.from_user.id}, {last_activity=}, {current_state=}")
    
    await state.update_data(last_activity=datetime.now().isoformat())
    logger.debug(f"Updated last activity for user {message.from_user.id}.")
    
    await state.clear()
    logger.debug(f"Cleared state for user {message.from_user.id}.")



