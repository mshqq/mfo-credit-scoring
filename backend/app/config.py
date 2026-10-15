import pydantic_settings.main
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "MFO Credit Scoring"
    debug: bool = False

    database_url: str = "sqlite:///./mfo.db"

    cors_origins: list[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ]

    static_dir: str = "static"
    images_dir: str = "static/images"

    model_config: pydantic_settings.main.SettingsConfigDict = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
