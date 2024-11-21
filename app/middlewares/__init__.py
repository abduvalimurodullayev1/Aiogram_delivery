from .logging import *
from sqlalchemy import create_engine
from app.middlewares.check_subscription import *
from app.middlewares.check_registration import *
from app.middlewares.db_middleware import DatabaseSessionMiddleware  # Middlewareni import qilish
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# PostgreSQL uchun DSN
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root123@localhost:5432/bot_aiogram"

# Engine yaratish
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal obyektini yaratish
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def setup_middlewares(dp):
    dp.update.outer_middleware(LoggingMiddleware())
    dp.update.outer_middleware(CheckRegistrationMiddleware())
    dp.update.outer_middleware(CheckRegistrationMiddleware())
    dp.update.outer_middleware(DatabaseSessionMiddleware(SessionLocal))  # SQLAlchemy sessiya middleware
