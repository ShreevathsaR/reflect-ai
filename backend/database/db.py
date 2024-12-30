from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os




load_dotenv()
DB_URL = os.getenv("DB_URL")



engine: AsyncEngine = create_async_engine(DB_URL, echo=True)

async_session_local = sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)