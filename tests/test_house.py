from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_predict_price():
    # 測試目標：驗證 ML 模型推論邏輯和 Pydantic 輸出格式
    r = client.post("/v2/house/predict", json={"size": 1200, "rooms": 3})
    assert r.status_code == 200
    # 測試目標：確保預測結果在合理的範圍內 (數據標記為 320000)
    assert 300000 <= r.json()["predicted_price"] <= 400000
