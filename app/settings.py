
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Sistema de Frota"
    database_url: str = "sqlite:///./frota.db"
    secret_key: str = "your-secret-key"
    
    class Config:
        env_file = ".env"

settings = Settings()
