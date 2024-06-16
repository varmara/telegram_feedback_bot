import os
from dotenv import load_dotenv
import logging
import locale

import asyncio
from aiogram import Bot, Dispatcher

from utils.functions import moscow_time
from handlers import start, help, message

def setup_logging():
    """
    Configures logging settings for the bot.
    """
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8') 

    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            logging.StreamHandler(),  # Log to console
            # Uncomment to also log to file:
            # logging.FileHandler("my_bot.log") 
        ]
    )

def load_env_variables():
    """
    Loads environment variables from the .env file and validates them.
    """
    load_dotenv(override=False)

    required_vars = ["TOKEN", "CHAT_ID", "TOPIC_ID"]
    for var in required_vars:
        if os.getenv(var) is None:
            raise ValueError(f"Environment variable {var} is missing. Please check your configuration.")

    return {
        "TOKEN": os.getenv("TOKEN"),
        "CHAT_ID": os.getenv("CHAT_ID"),
        "TOPIC_ID": int(os.getenv("TOPIC_ID")),  # Cast TOPIC_ID to int
    }

async def main():  
    # Setup logging first
    setup_logging()
    logger = logging.getLogger(__name__)

    # Load and validate environment variables 
    env_vars = load_env_variables()

    logging.info(f"{moscow_time()}: Set up environment variables.")

    bot = Bot(token=env_vars["TOKEN"])
    dp = Dispatcher()
    dp.include_routers(start.router, help.router, message.router) 

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
 
if __name__ == '__main__':
    asyncio.run(main())

