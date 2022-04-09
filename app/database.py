import os

from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# TODO: Find better way.
SQLALCHEMY_DATABASE_URL = os.environ.get('SQLALCHEMY_DATABASE_URL') or 'postgresql://user:password@postgres/db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

