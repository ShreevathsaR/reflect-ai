from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from database.db import Base



#table for users
class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    mbti_type = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc)) #'default=datetime.utc' didn't work: deprecation warning

    journal_entries = relationship('JournalEntry', back_populates='users')
    monthly_reports = relationship('MonthlyReport', back_populates='users')

#table for journal entries(by users)
class JournalEntry(Base):
    __tablename__ = 'journal_entries'

    entry_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    entry_text = Column(String, nullable=False)
    entry_date = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))

    user = relationship('User', back_populates='journal_entries')
    ai_responses = relationship('AIResponse', back_populates='journal_entries')
    sentiment_analysis = relationship('SentimentAnalysis', back_populates='journal_entry', uselist=False)

#table for responses from ai(for journal entry)
class AIResponse(Base):
    __tablename__ = 'ai_responses'

    response_id = Column(Integer, primary_key=True, index=True)
    entry_id = Column(Integer, ForeignKey('journal_entries.entry_id'), nullable=False)
    response_text = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))

    journal_entry = relationship('JournalEntry', back_populates='ai_responses')

#table for sentiment analysis(for journal entry)
class SentimentAnalysis(Base):
    __tablename__ = 'sentiment_analysis'

    sentiment_id = Column(Integer, primary_key=True, index=True)
    entry_id = Column(Integer, ForeignKey('journal_entries.entry_id'), nullable=False)
    sentiment_score = Column(Integer)
    sentiment_label = Column(String(50))
    created_at = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))

    journal_entry = relationship('JournalEntry', back_populates='sentiment_analysis')

#table for monthly report(for user)
class MonthlyReport(Base):
    __tablename__ = 'monthly_reports'

    report_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    report__date = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))
    report_data = Column(String, nullable=False)

    user = relationship('User', back_populates='monthly_reports')