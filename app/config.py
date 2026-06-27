from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", "app/.env"),
        env_file_encoding="utf-8",
    )

    database_url: str = "postgresql+asyncpg://xtract:xtract@localhost:5432/xtract"
    api_key: str = "dev-secret-key"
    openai_api_key: str = ""


settings = Settings()
