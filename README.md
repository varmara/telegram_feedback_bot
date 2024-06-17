# Telegram Bot for Gathering User Feedback

[![Python Version](https://img.shields.io/badge/python-3.10.12-blue.svg)](https://www.python.org/)
[![Aiogram Version](https://img.shields.io/badge/aiogram-3.7.0-green.svg)](https://docs.aiogram.dev/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


This Telegram bot is designed to simplify the process of collecting and moderating user-submitted content for Telegram channels. 

The bot collects messages from 121 chats with users and forward them to a specific topic (message thread) within a designated Telegram admin group chat. It's built using the aiogram 3.x framework and follows a modular structure for easy maintenance and extension.

## Features

* **Message Forwarding:** Forwards messages from users in private chats to a specific topic in a group chat.
* **Customizable:** Easily configure the target group chat and topic using environment variables.
* **Formatting Preservation:** Preserves the original formatting of forwarded messages.

**Planned enhancements:** [TODO](./TODO.md)

## Installation

1. **Clone the Repository:**

2. **Set up a Virtual Environment:**

    In the project directory, create a virtual environment:
    ```bash
    python -m venv venv
    ```

    Activate your virtual environment:
    ```bash
    source venv/bin/activate  # On macOS/Linux
    .\venv\Scripts\activate  # On Windows
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Create a .env file:**

In the project root, create a .env file, or rename .env.example.

```
TOKEN=your_bot_token
CHAT_ID=your_group_chat_id 
TOPIC_ID=your_topic_id (message thread id)
```

2. **Fill in necessary details:**

Obtain your bot token from BotFather on Telegram.

You can find the group chat ID by adding a bot like @userinfobot to your group and using the /id command.

The topic ID (message thread id) is a numeric identifier associated with a specific message thread within a group.

## Running the Bot Locally

In the project directory execute:

```bash
python bot.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENCE) file for details.










