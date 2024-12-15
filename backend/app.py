from fastapi import FastAPI
from dotenv import load_dotenv
import os
# import aiohttp
from contextlib import asynccontextmanager

# from backend.routes.ai_features import router as ai_router
from database.db_conn import connect_db



load_dotenv()

HF_TOKEN=os.getenv("HUGGING_FACE_TOKEN")
API_URL=os.getenv("API_URL")


prompt = (
    """The user has the personality type INFJ. They are feeling anxious today,
    and their journal sentiment is negative. The journal discusses topics like 
    career, stress, and time management. Based on this information, generate a reflective journal prompt."""
)

HEADER={"Authorization":f"Bearer {HF_TOKEN}"}

@asynccontextmanager
async def lifespan(app: FastAPI):
     print("server is running...")
     await connect_db()
     yield
     print("server is shutting down...")

app = FastAPI(lifespan=lifespan)
# app.include_router(ai_router, prefix="/api/v1", tags=["AI"])


