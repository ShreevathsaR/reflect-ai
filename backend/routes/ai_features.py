# from fastapi import APIRouter, HTTPException
# from app.services.ai_service import generate_ai_response
# # from app.models.ai_models import AIRequest, AIResponse

# router = APIRouter()

# @router.post("/prompt", response_model=AIResponse)
# async def analysis(request: AnalysisRequest):
#     try:
#         response = generate_ai_response(request)
#         return {"prompt": response}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
