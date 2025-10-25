from pydantic import BaseModel, Field

class TextInput(BaseModel):
    # Pydantic 實踐：使用 Field 進行約束，防止 DoS 攻擊 (如輸入過長文字)
    text: str = Field(..., min_length=1, max_length=500, example="I love this!")
