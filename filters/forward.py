import os
from typing import Union, Dict, Any

from aiogram.filters import BaseFilter
from aiogram.types import Message

class ForwardToFilter(BaseFilter):
    async def __call__(self, message: Message) -> Union[bool, Dict[str, Any]]:
        # Retrieve CHAT_ID and TOPIC_ID from environment variables
        CHAT_ID = os.getenv("CHAT_ID")
        TOPIC_ID = int(os.getenv("TOPIC_ID", "0")) 
        return {"chat_id": CHAT_ID, "topic_id": TOPIC_ID}  # Return as a dictionary