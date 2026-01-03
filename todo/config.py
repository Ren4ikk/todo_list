import os
from typing import ClassVar

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    app_name: ClassVar = os.getenv("NAME_APP")
    db_url: ClassVar = os.getenv("SQLALCHEMY_DATABASE_URL")


    class Config:
        env_file: str = "../.env"


settings = Settings()
