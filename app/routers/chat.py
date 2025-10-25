from fastapi import APIRouter, HTTPException
from openai import OpenAI
from app.schemas.text import TextInput
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()
router = APIRouter()
# MLOps 實踐：從環境變數讀取 API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatResponse(BaseModel):
    reply: str
    usage_tokens: int # 實踐：追蹤 Token 使用量，便於成本監控

@router.post("/chat", response_model=ChatResponse)
async def chat(request: TextInput):
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(status_code=500, detail={"error": "OPENAI_API_KEY not set. Check .env file."})
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # 實踐：選擇合適的模型
            # 實踐：基本 Prompt Engineering - 僅傳遞使用者訊息
            messages=[{"role": "user", "content": request.text}],
            max_tokens=150
        )
        return ChatResponse(reply=response.choices[0].message.content, usage_tokens=response.usage.total_tokens)
    except Exception as e:
        # 實踐：處理外部 API 呼叫失敗的錯誤
        raise HTTPException(status_code=500, detail={"error": str(e)})
