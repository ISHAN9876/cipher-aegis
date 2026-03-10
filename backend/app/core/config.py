from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    UNSPLASH_KEY: str
    PEXELS_KEY: str
    SUPABASE_URL: str
    SUPABASE_SERVICE_KEY: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()