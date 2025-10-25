from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_rag_ask():
    # 測試目標：驗證 RAG 檢索邏輯是否從文件 (data/documents.txt) 中找到關鍵資訊
    r = client.post("/v4/rag/ask", json={"text": "refund"})
    assert r.status_code == 200
    assert "refund" in r.json()["answer"].lower()
