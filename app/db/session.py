from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
import os

DB_URL = os.getenv("DATABASE_URL", "sqlite:///./blog.db")

if not DB_URL:
    raise ValueError("❌ DATABASE_URL is not set in environment variables")

engine = create_engine(DB_URL, echo = True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

class Base(DeclarativeBase):
    pass

def init_db():
    from .models import User, Post, Comment
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()