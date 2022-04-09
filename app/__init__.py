
from fastapi import Depends, FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .config import settings
from . import models

def create_app():
    engine = create_engine(
        settings.sqlalchemy_data_url
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

    # get db session
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    # NOTE: Does sql need create first ?
    # models.Base.metadata.create_all(bind=engine)
    return FastAPI(
        dependencies=[Depends(get_db)],
    )
