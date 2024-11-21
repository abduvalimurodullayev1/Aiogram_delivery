import config
import asyncpg


class DBManager:
    def __init__(self):
        self.pool = None

    async def connect(self):
        """Connect to the database"""
        self.pool = await asyncpg.create_pool(dsn=config.DB_DNS)

    async def disconnect(self):
        """Disconnect from the database"""
        if self.pool is not None:
            await self.pool.close()

    async def fetch(self, query: str, *args):
        """Fetch a list of objects from the database"""
        async with self.pool.acquire() as connection:
            results = await connection.fetch(query, *args)
            return [dict(result) for result in results]

    async def fetch_one(self, query: str, *args):
        """Fetch a single object from the database"""
        async with self.pool.acquire() as connection:
            result = await connection.fetchrow(query, *args)
            return dict(result) if result else None

    async def execute(self, query, *args):
        """Execute a SQL command"""
        async with self.pool.acquire() as connection:
            await connection.execute(query, *args)

    async def create_tables(self):
        queries = [
            """
            CREATE TABLE IF NOT EXISTS users (
                telegram_id BIGINT PRIMARY KEY,
                language VARCHAR(16),
                phone VARCHAR(32),
                name VARCHAR(255),
                username VARCHAR(255)
            );
            """
        ]

        for query in queries:
            await self.execute(query)

    async def get_user(self, telegram_id):
        """Fetch a user by Telegram ID"""
        query = "SELECT * FROM users WHERE telegram_id = $1"
        return await self.fetch_one(query, telegram_id)

    async def create_user(self, *args):
        query = "INSERT INTO users (telegram_id, language, phone, name, username) VALUES ($1, $2, $3, $4, $5)"
        return await self.execute(query, *args)


db = DBManager()
