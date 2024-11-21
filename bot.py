import config
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from app.handlers import setup_handlers
from app.middlewares import setup_middlewares
from app.utils.db_manager import db


async def main():
    redis = await Redis.from_url(config.REDIS_URL)

    await db.connect()
    await db.create_tables()

    bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=RedisStorage(redis=redis))

    setup_middlewares(dp)

    setup_handlers(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    await db.disconnect()