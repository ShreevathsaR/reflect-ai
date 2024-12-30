from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import logging
import os

from database.db import async_session_local
from database.db_model import User, JournalEntry, AIResponse, SentimentAnalysis, MonthlyReport




db_crud_logger = logging.getLogger("db_crud_logger")
db_crud_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(os.path.join('database', 'db.log'))
file_handler.setFormatter(logging.Formatter('%(asctime)s / %(levelname)s / %(message)s'))
db_crud_logger.addHandler(file_handler)



#create user
async def create_user(session: AsyncSession, email: str, password: str, mbti_type: str):
    try:
        user = User(email=email, password=password, mbti_type=mbti_type)
        session.add(user)
        await session.commit()
        db_crud_logger.info(f"user {email} created successfully")
        return user
    except Exception as e:
        db_crud_logger.exception(f"error creating user: {e}")
        await session.rollback()
        raise e
    

#create journal entry for user
async def create_journal_entry(session: AsyncSession, user_id: int, journal: str):
    try:
        journal_entry = JournalEntry(user_id=user_id, journal=journal)
        session.add(journal_entry)
        await session.commit()
        db_crud_logger.info(f"journal entry created successfully for user_id: {user_id}")
        return journal_entry
    except Exception as e:
        db_crud_logger.exception(f"error creating journal entry: {e}")
        await session.rollback()
        raise e
    

#ai reponses for users
async def create_ai_responses(session: AsyncSession, entry_id: int, response: str):
    try:
        ai_response = AIResponse(entry_id=entry_id, response=response)
        session.add(ai_response)
        await session.commit()
        db_crud_logger.info(f"ai response created successfully for journal {entry_id}")
        return ai_response
    except Exception as e:
        db_crud_logger.exception(f"error creating ai response: {e}")
        await session.rollback()
        raise e


#sentiment analysis of a journal
async def create_sentiment_analysis(session: AsyncSession, entry_id: int, sentiment_score: int, sentiment_label: str):
    try:
        sentiment_analysis = SentimentAnalysis(sentiment_score=sentiment_score, sentiment_label=sentiment_label)
        session.add(sentiment_analysis)
        await session.commit()
        db_crud_logger.info(f"sentiment analysis created successfully for journal id {entry_id}")
    except Exception as e:
        db_crud_logger.exception(f"error creating sentiment analysis: {e}")
        await session.rollback()
        raise e
    

#monthly report for an user
async def create_monthly_report(session: AsyncSession, user_id: int, report: str):
    try:
        monthly_report = MonthlyReport(user_id=user_id, report=report)
        session.add(monthly_report)
        await session.commit()
        db_crud_logger.info(f"monthly report successfully created for user {user_id}")
    except Exception as e:
        db_crud_logger.exception(f"failed to create monthly report: {e}")
        await session.rollback()
        raise e