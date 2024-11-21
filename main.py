import asyncio
import logging
from loguru import logger
from bot import main as run_bot
from db_manager import fetch_users  

logger.remove()  
logger.add("app.log", level="INFO", rotation="500 MB", compression="zip")  

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    event_loop = asyncio.get_event_loop()

    try:
        event_loop.create_task(run_bot())

        users = asyncio.run(fetch_users()) 
        logger.info(f"Fetched users: {users}")

        event_loop.run_forever()
    except KeyboardInterrupt:
        logger.info("Bot to'xtatildi.")
        event_loop.stop()
    except Exception as e:
        logger.error(f"Xatolik yuz berdi: {e}") 
