from fastapi import APIRouter, HTTPException
from app.schemas.text import TextInput
from pydantic import BaseModel
from app.models.rag import rag

router = APIRouter()

class AnswerResponse(BaseModel):
    answer: str # 實踐：RAG 系統輸出為檢索到的「答案」

@router.post("/ask", response_model=AnswerResponse)
async def ask_question(request: TextInput):
    try:
        # 實踐：將使用者問題傳入 RAG 系統
        answer = rag.query(request.text)
        return AnswerResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail={"error": str(e)})
