from fastapi import APIRouter, HTTPException
from transformers import pipeline
from app.schemas.text import TextInput
from pydantic import BaseModel
from app.utils.logger import get_logger

router = APIRouter()
logger = get_logger(__name__)

# 模型初始化：由於模型已在 Dockerfile 中預載，這裡的載入會非常快
classifier = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

class PredictionOutput(BaseModel):
    label: str
    score: float

@router.post("/predict", response_model=PredictionOutput)
async def predict_sentiment(request: TextInput):
    try:
        result = classifier(request.text)[0]
        label = result['label'].upper()
        # 實踐：將模型的內部標籤 (e.g., LABEL_2) 轉換為業務友好的標籤 (e.g., POSITIVE)
        if label not in ["POSITIVE", "NEGATIVE"]: label = "NEUTRAL" 
        return PredictionOutput(label=label, score=result['score'])
    except Exception as e:
        # 實踐：標準化錯誤處理，回傳 HTTP 500
        logger.error(f"Sentiment prediction failed: {e}")
        raise HTTPException(status_code=500, detail={"error": str(e)})
