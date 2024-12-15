from fastapi import APIRouter, HTTPException
from services.ai_features import generate_ai_response
from models.ai_features import AIRequest, AIResponse, JournalText

router = APIRouter()

@router.post("/prompt")
async def analysis(journal_text: JournalText):
    try:
        # print(journal_text)
        response = generate_ai_response(journal_text)
        return {"prompt": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
