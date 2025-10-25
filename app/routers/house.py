from fastapi import APIRouter, HTTPException
from app.schemas.house import HouseInput, PricePrediction
from app.models.house_price import load_model

router = APIRouter()
try:
    # 模型初始化：在 API 啟動時一次性載入
    model = load_model()
except FileNotFoundError:
    model = None

@router.post("/predict", response_model=PricePrediction)
async def predict_price(data: HouseInput):
    if model is None:
        # 實踐：模型未載入時的錯誤提示
        raise HTTPException(status_code=500, detail={"error": "Model not loaded. If running locally, please run training script first."})
    
    features = [[data.size, data.rooms]]
    price = model.predict(features)[0]
    # 實踐：確保輸出格式為浮點數，並進行四捨五入
    return PricePrediction(predicted_price=round(float(price), 2))
