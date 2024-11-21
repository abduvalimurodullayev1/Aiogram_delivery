from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, Time
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root123@localhost:5432/bot_aiogram"
from sqlalchemy.orm import Session
from aiogram import Dispatcher
from contextlib import contextmanager

from app.middlewares.db_middleware import DatabaseSessionMiddleware
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
dp = Dispatcher()
dp.update.middleware(DatabaseSessionMiddleware(SessionLocal))


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
        
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    phone_number = Column(String)
    full_name = Column(String)
    language = Column(String)
    telegram_id = Column(Integer, unique=True)
    username = Column(String)
  
  
  
  
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    order = Column(String)
    
    
class Branches(Base):
    __tablename__ = 'branches'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_time = Column(Time)
    end_time = Column(Time)
    location = Column(String)
    

class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    image = Column(String, nullable=True)
    
    @classmethod
    def all_menu(cls):
        with get_db() as session:
            try:
                return session.query(cls).all()
            except Exception as e:
                session.rollback()
                print(e)
                return []