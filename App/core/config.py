from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Settings(BaseSettings):
    APP_NAME: str

    SECRET_KEY: str
    ALGORITHM: str

    DATABASE_URL: str

    REDIS_HOST: str

    REDIS_PORT: int

    NATS_URL: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()

print("Current Directory:", os.getcwd())
print("ENV Exists:", os.path.exists(".env"))