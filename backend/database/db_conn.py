import asyncpg
import asyncio
from sqlalchemy.exc import OperationalError
from database.db import engine, Base, DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER



async def create_db():
    try:
        conn = await asyncpg.connect(
            user='postgres',
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )

        # Create the database
        await conn.execute(f"CREATE DATABASE {DB_NAME}")
        print(f"database {DB_NAME} created successfully")

        await conn.close()

    except Exception as e:
        print(f"error while creating the database: {e}")
        raise e #raising the error to use it elsewhere if needed


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

    except OperationalError as e:
        if "database \"{}\" does not exist".format(DB_NAME) in str(e):
            print(f"database {DB_NAME} does not exist. Creating it now...")
            await create_db()
            await asyncio.sleep(3) #ensuring the connection is successful by delaying the process
            return await connect_db() 
        else:
            print(f"Error connecting to the database: {e}")
            raise e 

