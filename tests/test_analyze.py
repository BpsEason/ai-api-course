from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_analyze():
    # 測試目標：驗證多重 NLP 任務 (情緒和關鍵字) 的整合與輸出格式
    r = client.post("/v5/analyze", json={"text": "FastAPI is amazing for building crawlers"})
    assert r.status_code == 200
    data = r.json()
    assert "sentiment" in data
    assert "keywords" in data
    assert data["sentiment"] in ["positive", "neutral"]
    assert "fastapi" in [k.lower() for k in data["keywords"]]
