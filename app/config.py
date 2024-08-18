from pydantic_settings import BaseSettings
from dotenv import dotenv_values

c = dotenv_values()


class Settings(BaseSettings):
    app_name: str = "My Recipes and Shopping Lists"
    db_name: str = "recipes_and_shopping_lists"
    mongo_db_connection_string: str = c["MONGO_DB_CONNECTION_STRING"]


settings = Settings()
