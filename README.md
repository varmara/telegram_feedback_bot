# Telegram Bot for Gathering User Feedback

[![Python Version](https://img.shields.io/badge/python-3.10.12-blue.svg)](https://www.python.org/)
[![Aiogram Version](https://img.shields.io/badge/aiogram-3.7.0-green.svg)](https://docs.aiogram.dev/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


This Telegram bot is designed to simplify the process of collecting and moderating user-submitted content  and feedback for Telegram channels. 

The bot collects messages from one-to-one chats with users and forward them to a specific topic (message thread) within a designated Telegram admin group chat. It's built using the aiogram 3.x framework and follows a modular structure for easy maintenance and extension.

## Features

- Forwards messages from private chats with the users to a specific topic in an admin group.
- Easily configure the target group chat and topic using environment variables.
- Preserves the original formatting of forwarded messages.
- Can be easily localised using the "fluent" python library. Currently ru and en interface languages are supported.

**Planned enhancements:** [TODO](./TODO.md)

## Getting Started

1. **Clone the repository:**

```bash
git clone [repository url]
cd your-telegram-bot
```

2. **Environment configuration:**

- Create a `.env` file in the project root directory.
- Fill in the required environment variables. You can find an example in a `.env.example` file.

## Development Setup

### (A) Running with a docker container locally + local VS Code

1. **Prerequisites:**

* **Docker:** Make sure you have Docker installed and running on your system. You can find instructions on the official Docker website: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
* **Docker Compose:** This tool simplifies multi-container Docker applications. It's likely installed with Docker, but you can confirm by running `docker-compose --version`.
* **VS Code extensions:** `Dev Containers` and `Docker`

1. **Build the development image:**

```bash
docker-compose build bot_dev  # Use the service name from docker-compose.yml
```

2. **Run the development container:**

```bash
docker-compose up -d --build bot_dev 
docker exec -it bot_dev bash
```

Your Docker container should be running. The mounted volume (see `Dockerfile.dev`) will allow you to directly edit files on your local machine using VS Code, and the changes will be immediately reflected in the container.

3. **VS Code setup:**

To open the container in VS Code:

- In the Docker extension sidebar, right-click on the running `bot_dev` container and choose "Attach Visual Studio Code." VS Code will open a new window connected to your container.
- You can also use the Command Palette (Ctrl+Shift+P) and type "Remote-Containers: Attach to Running Container…"

4. **Run the bot:**

In the attached VS Code window, you'll have a terminal directly into your container. You can run the bot as normal:

```bash
python3 -m bot
```

### (B) Running from a .devcontainer in the VS Code

1. **Prerequisites:**

* **Docker:** Make sure you have Docker installed and running on your system. You can find instructions on the official Docker website: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
* **Docker Compose:** This tool simplifies multi-container Docker applications. It's likely installed with Docker, but you can confirm by running `docker-compose --version`.
* **VS Code extensions:** `Dev Containers` and `Docker`

2. **Open container in VS Code:**
    - Open your project folder in VS Code. The `.devcontainer.json` file should be present in a `.devcontainer` subdirectory.
    - To start the dev container initially use Command Palette (Ctrl+Shift+P) -> "Remote-Containers: Reopen in Container".
    - VS Code will build the container image (if it hasn't been built before) and create a new VS Code window connected to it.
    - The terminal within this window is connected to the container.
    - VS Code automatically installs the extensions specified in the `devcontainer.json`.
3. **Rebuilding the container:**
    - If you've made changes to your `Dockerfile.dev` or `requirements.txt`, you will have to rebuild the dev container image. Command Palette -> "Remote-Containers: Rebuild Container."
4. **Run the bot:**

In the attached VS Code window, you'll have a terminal directly into your container. You can run the bot as normal:

```bash
python3 -m bot
```

### (C) Running with a virtual environment locally

If you prefer not to use Docker, you can follow these steps:

1. **Set up a virtual environment:**

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate  # On macOS/Linux
.\venv\Scripts\activate   # On Windows
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the bot:**

```bash
python3 -m bot
```


## License

This project is licensed under the MIT License - see the [LICENSE](./LICENCE) file for details.










