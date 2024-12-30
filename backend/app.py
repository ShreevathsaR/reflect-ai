from fastapi import FastAPI
import logging
from contextlib import asynccontextmanager

from database.db_conn import connect_db




logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("server is running...")

    db_conn = None
    try:
        db_conn = await connect_db()
        logger.info("database connection pool initialized")
        yield
    except Exception as e:
        logger.error(f"error during server startup: {e}", exc_info=True)
        raise e
    finally:
        if db_conn:
            logger.info("closing the database connection pool...")
            await db_conn.close()
            logger.info("database connection pool closed")
        logger.info("shutting down...")


app = FastAPI(lifespan=lifespan)