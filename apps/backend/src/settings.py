from enum import StrEnum
from typing import Literal
from pydantic_settings import SettingsConfigDict, BaseSettings


class Env(StrEnum):
    """Describes the current runtime environment."""
    DEV = "DEV"
    PROD = "PROD"
    TEST = "TEST"

LogLevel = Literal["TRACE", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

class Settings(BaseSettings):
    """Application configuration loaded from the environment."""
    model_config = SettingsConfigDict(env_prefix="AS_", env_file=".env")

    env: Env = Env.DEV
    """Application runtime environment."""

    log_level: LogLevel = "INFO"
    """Logging verbosity level."""

    server_address: str = "127.0.0.1"
    """Host address for the server."""

    server_port: int = 8080
    """Server port."""

    database_url: str = "sqlite:///db.sqlite"
    """Database connection string."""


def load_settings() -> Settings:
    """Load application settings from environment and .env file."""
    return Settings()