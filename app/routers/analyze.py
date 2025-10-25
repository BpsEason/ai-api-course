from fastapi import APIRouter, HTTPException
from app.schemas.text import TextInput
from pydantic import BaseModel
from app.models.nlp_processor import analyzer

router = APIRouter()

class AnalysisResult(BaseModel):
    sentiment: str
    keywords: List[str]

@router.post("/analyze", response_model=AnalysisResult)
async def analyze_text(request: TextInput):
    try:
        result = analyzer.analyze(request.text)
        return AnalysisResult(**result)
    except Exception as e:
        logger.error(f"Analysis failed: {e}")
        raise HTTPException(status_code=500, detail={"error": str(e)})
