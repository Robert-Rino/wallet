from app.database import SQLALCHEMY_DATABASE_URL
from pydantic import BaseSettings


class Settings(BaseSettings):
    secret_key :str='secret'
    sqlalchemy_data_url :str='postgresql://user:password@postgres/db'

settings = Settings()
