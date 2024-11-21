from aiogram import BaseMiddleware
from sqlalchemy.orm import sessionmaker
from typing import Callable, Any


class DatabaseSessionMiddleware(BaseMiddleware):
    def __init__(self, db_sessionmaker: sessionmaker):
        super().__init__()
        self.db_sessionmaker = db_sessionmaker

    async def __call__(self, handler: Callable, event: Any, data: dict):
        session = self.db_sessionmaker()
        try:
            data["session"] = session  # Sessiyani uzatamiz
            response = await handler(event, data)
            session.commit()  # O'zgarishlarni saqlash
            return response
        except Exception:
            session.rollback()  # Xatolik bo'lsa, o'zgarishlarni bekor qilish
            raise
        finally:
            session.close()  # Sessiyani yopish
