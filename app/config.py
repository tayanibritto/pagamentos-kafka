from pydantic_settings import BaseSettings, SettingsConfigDict

# Classe que busca os valores nas variáveis de ambiente
class Settings(BaseSettings):
    api_title: str
    api_version: str

    kafka_topic: str
    kafka_bootstrap_servers: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()