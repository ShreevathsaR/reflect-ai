from pydantic import BaseModel
from typing import List

class AIRequest(BaseModel):
    personality: str
    emotion: str
    sentiment: str
    keywords: List[str]

class AIResponse(BaseModel):
    prompt: str

class AnalysisRequest(BaseModel):
    text: str

class JournalText(BaseModel):
    text: list[str]