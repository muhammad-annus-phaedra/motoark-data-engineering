from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = ""
    log_level: str = "INFO"


def get_settings() -> Settings:
    return Settings()
