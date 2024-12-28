from sqlalchemy import text

from database.db import engine
from database.db_model import Base




async def create_table():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("tables created successfully")
    except Exception as e:
        print(f"error while creating tables: {e}")
        raise e


async def connect_db():
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            if result.scalar() == 1:
                print(f"connected to the database successfully")
            else:
                print("failed to verify connection to the database")
    except Exception as e:
        print(f"error connecting to the database: {e}")
        raise e