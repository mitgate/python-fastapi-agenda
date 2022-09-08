"""SETTINGS
Atencao, efetua leitura do dotenv)
"""

# # Installed # #
import pydantic

__all__ = ("api_settings", "mongo_settings")


class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = ".env"


class APISettings(BaseSettings):
    title: str = "Pessoas API"
    host: str = "0.0.0.0"
    port: int = 5000
    log_level: str = "INFO"

    class Config(BaseSettings.Config):
        env_prefix = "API_"


class MongoSettings(BaseSettings):
    uri: str = "mongodb://127.0.0.1:27017"
    database: str = "fastapi_mongodb_agenda"
    collection: str = "pessoas"

    class Config(BaseSettings.Config):
        env_prefix = "MONGO_"


api_settings = APISettings()
mongo_settings = MongoSettings()
