import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

logger = logging.getLogger(__name__)

class UserInfoMiddleware(BaseMiddleware):
    
    async def __call__(
            self, 
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
            event: TelegramObject, 
            data: Dict[str, Any]
            ) -> Any:
        logger.debug(
            "Enter into middleware %s, event type %s",
            __class__.__name__,
            event.__class__.__name__
        )
        if isinstance(event, Message):
            user_id = getattr(event.from_user, "id", None)
            user_full_name = getattr(event.from_user, "full_name", "Unknown")
            username = getattr(event.from_user, "username", "unknown_username")
            logger.debug(f"{user_id=} {user_full_name=} {username=}: New message.")
       
        result = await handler(event, data)
        
        logger.debug("Exit from middleware.")
        
        return result
 