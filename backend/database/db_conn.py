import asyncpg
from database.db import engine, Base, DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER



async def create_tables():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("tables created successfully")

    except Exception as e:
        print(f"error while creating tables: {e}")
        raise e


async def connect_db():
    try:
        conn = await asyncpg.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )
        await create_tables()  # Create tables if they don't exist
        print(f"connected to the database '{DB_NAME}' successfully")
        return conn

    except Exception as e:
        print(f"error connecting to the database: {e}")
        raise e