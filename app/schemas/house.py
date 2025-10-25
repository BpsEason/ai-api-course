from pydantic import BaseModel, Field

class HouseInput(BaseModel):
    # Pydantic 實踐：對輸入數值進行範圍驗證，防止無效輸入
    size: float = Field(..., gt=0, example=1200)
    rooms: int = Field(..., ge=1, le=10, example=3)

class PricePrediction(BaseModel):
    predicted_price: float
