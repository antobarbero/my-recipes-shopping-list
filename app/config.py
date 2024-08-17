from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="..\\.env", env_file_encoding="utf-8")
    app_name: str = "My Recipes and Shopping Lists"
    mongo_db_connection_string: str


settings = Settings()
