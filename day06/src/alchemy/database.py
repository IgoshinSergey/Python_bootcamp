from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from .config import settings


engine = create_engine(
    url=settings.db_url_psycopg
)
session_factory = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass
