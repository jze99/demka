from pydantic.generics import GenericModel  
import re
import yaml
from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str = "localhost"  
    DB_PORT: int = 5432 
    DB_USER: str = "tester"
    DB_PASS: str = "tester"
    DB_NAME: str = "test"

    @property 
    def DATABASE_URL_asyncpg(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    @property 
    def DATABASE_URL_syncpg(self) -> str:
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
class Config:
    env_file = "venv"  # Укажите файл окружения

# Загрузка настроек из .env файла
settings = Settings()
