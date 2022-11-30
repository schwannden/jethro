from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    BASIC_AUTH_USER: str
    BASIC_AUTH_PASSWORD: str

    GOOGLE_CLOUD_PROJECT: str
    SENTRY_DSN_SERVER: Optional[str] = None


settings = Settings()
