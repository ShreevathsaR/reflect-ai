from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone




Base = declarative_base()




""" 
utilizes typehint with Mapped & mapped_column()
Mapped[...] (typehint), mapped_column(...) ----> map type = map this attributes to the column
"""

# Table for users
class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    mbti_type: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))
    #created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default="CURRENT_TIMESTAMP") #for database-managed timestamps

    journal_entries = relationship('JournalEntry', back_populates='user')
    monthly_reports = relationship('MonthlyReport', back_populates='user')


# Table for journal entries (by users)
class JournalEntry(Base):
    __tablename__ = 'journal_entries'

    entry_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.user_id'), nullable=False)
    entry_text: Mapped[str] = mapped_column(String, nullable=False)
    entry_date: Mapped[datetime] = mapped_column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))

    user = relationship('User', back_populates='journal_entries')
    ai_responses = relationship('AIResponse', back_populates='journal_entry')
    sentiment_analysis = relationship('SentimentAnalysis', back_populates='journal_entry', uselist=False)


# Table for responses from AI (for journal entry)
class AIResponse(Base):
    __tablename__ = 'ai_responses'

    response_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    entry_id: Mapped[int] = mapped_column(Integer, ForeignKey('journal_entries.entry_id'), nullable=False)
    response_text: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))

    journal_entry = relationship('JournalEntry', back_populates='ai_responses')


# Table for sentiment analysis (for journal entry)
class SentimentAnalysis(Base):
    __tablename__ = 'sentiment_analysis'

    sentiment_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    entry_id: Mapped[int] = mapped_column(Integer, ForeignKey('journal_entries.entry_id'), nullable=False)
    sentiment_score: Mapped[int] = mapped_column(Integer)
    sentiment_label: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))

    journal_entry = relationship('JournalEntry', back_populates='sentiment_analysis')


# Table for monthly report (for user)
class MonthlyReport(Base):
    __tablename__ = 'monthly_reports'

    report_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.user_id'), nullable=False)
    report_date: Mapped[datetime] = mapped_column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))
    report_data: Mapped[str] = mapped_column(String, nullable=False)

    user = relationship('User', back_populates='monthly_reports')