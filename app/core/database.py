from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import settings
from typing import Generator

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False)

class Base(DeclarativeBase):
    pass

def get_db() -> Generator:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()