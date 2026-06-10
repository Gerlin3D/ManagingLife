from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "PainTrack Mini API"
    api_prefix: str = "/api"
    frontend_origin: str = "http://localhost:5173"
    database_url: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()