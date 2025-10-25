from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_predict_positive():
    # 測試目標：驗證 API 格式和情緒分類的準確性 (即使是預訓練模型)
    r = client.post("/v1/sentiment/predict", json={"text": "I love this!"})
    assert r.status_code == 200
    data = r.json()
    assert "label" in data
    assert "score" in data
    assert data["label"] in ["POSITIVE", "NEUTRAL"]
