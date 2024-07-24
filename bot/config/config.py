import logging
from enum import Enum
from os import path
from pathlib import Path
from typing import Optional, Tuple, Type

from pydantic import BaseModel, Field, SecretStr
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)

logger = logging.getLogger(__name__)


def get_config_dir() -> Path:
    config_dir: Path = Path(__file__).resolve().parents[1]
    if not config_dir.is_dir():
        raise NotADirectoryError(f"Invalid config directory: {config_dir}")
    if not path.isfile(config_dir / ".env"):
        raise ValueError(f"Config directory ({config_dir}) is missing .env file")
    if not path.isfile(config_dir / "config_bot.yaml"):
        raise ValueError(
            f"Config directory ({config_dir}) is missing config_bot.yaml file"
        )
    return config_dir


class RedirectModeEnum(str, Enum):
    TOPIC = "topic"
    CHAT = "chat"


class BotSettings(BaseModel):
    token: SecretStr
    admin_chat_id: SecretStr
    redirect_mode: RedirectModeEnum = Field(default=RedirectModeEnum.CHAT)
    admin_topic_id: Optional[int] = Field(default=None)
    admin_time_zone: str = Field(default="Europe/Moscow")
    language: str

class RedisSettings(BaseModel):
    dsn: str


class PostgresSettings(BaseModel):
    # connection string: postgresql+psycopg://bot:password@db_host:5432/telegram
    db_schema: str  # e.g., postgresql+psycopg
    user: str  # e.g., bot
    password: SecretStr  # e.g., password
    host: str  # e.g., db_host
    port: int  # e.g., 5432
    database: str  # e.g., telegram
    is_echo: bool  # e.g., yes, see config

    @property
    def connection_string(self) -> str:
        return f"{self.db_schema}://{self.user}:{self.password.get_secret_value()}@{self.host}:{self.port}/{self.database}"


class Settings(BaseSettings, case_sensitive=True):
    model_config = SettingsConfigDict(
        env_file=Path(get_config_dir()) / ".env",
        extra="ignore",
        env_nested_delimiter="__",
        yaml_file=Path(get_config_dir()) / "config_bot.yaml",
    )
    bot: BotSettings
    redis: RedisSettings
    postgres: PostgresSettings

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return env_settings, dotenv_settings, YamlConfigSettingsSource(settings_cls)


def get_settings() -> Settings:

    if get_config_dir():
        logger.debug("Getting settings.")
        return Settings()  # type: ignore
    else:
        raise FileNotFoundError("Config directory not found")
