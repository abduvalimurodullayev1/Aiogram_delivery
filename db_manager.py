import asyncpg
from asyncpg.pool import create_pool
import asyncio

# PostgreSQL ulanish ma'lumotlari
DATABASE_URL = "postgresql://postgres:root123@localhost:5432/bot_aiogram"

# Ulanishlar bazasini yaratish
async def get_pool():
    pool = await create_pool(
        dsn=DATABASE_URL,
        min_size=5,  # Minimal ulanishlar soni
        max_size=10  # Maksimal ulanishlar soni
    )
    return pool

async def fetch_users():
    pool = await get_pool()
    async with pool.acquire() as conn:
        result = await conn.fetch("SELECT * FROM users")
        return result

# Asinxron kodni ishga tushurish
async def main():
    users = await fetch_users()
    print(users)

if __name__ == "__main__":
    asyncio.run(main())
