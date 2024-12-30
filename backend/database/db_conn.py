from sqlalchemy import text
import logging
import os

from database.db import engine
from database.db_model import Base




db_logger = logging.getLogger("db_logger")
db_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(os.path.join('database', 'db.log'))
file_handler.setFormatter(logging.Formatter('%(asctime)s / %(levelname)s / %(message)s'))
db_logger.addHandler(file_handler)



async def create_table():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        db_logger.info("tables created successfully or already exists")
    except Exception as e:
        db_logger.exception(f"error while creating tables: {e}")
        raise e


async def connect_db():
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            if result.scalar() == 1:
                db_logger.info("connected to the database successfully")
            else:
                db_logger.error("failed to verify connection to the database")
            await create_table()
    except Exception as e:
        db_logger.exception(f"error connecting to the database: {e}")
        raise e