from pydantic import BaseSettings
from typing import Callable
from dotenv import load_dotenv

class Settings(BaseSettings):
    ENV: str
    PYTHONPATH: str
    LOG_LEVEL: str
    DATABASE_PG_URL_USER: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int
    JWT_ALGORITHM: str
    JWT_SECRET_KEY: str
    WEB_APP_DEBUG: bool
    WEB_APP_DESCRIPTION: str
    WEB_APP_TITLE: str
    WEB_APP_VERSION: str
    WEB_SERVER_HOST: str
    WEB_SERVER_PORT: int
    WEB_SERVER_RELOAD: bool

def _configure_initial_settings() -> Callable[[], Settings]:
    load_dotenv()
    settings = Settings()

    def get_settings() -> Settings:
        return settings

    return get_settings

get_settings = _configure_initial_settings()