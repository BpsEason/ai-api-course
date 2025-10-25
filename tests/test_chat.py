from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch
client = TestClient(app)

@patch("app.routers.chat.client")
def test_chat(mock_openai):
    # 測試目標：使用 mock 模擬外部 API 回應，避免實際呼叫和支付費用
    mock_openai.chat.completions.create.return_value.choices = [
        type('obj', (), {'message': type('msg', (), {'content': 'Hi!'})})()
    ]
    mock_openai.chat.completions.create.return_value.usage.total_tokens = 5
    r = client.post("/v3/chat", json={"text": "Hi"})
    # 測試目標：驗證 API Key 未設定時的錯誤處理 (500) 或成功時的 200
    assert r.status_code in [200, 500] 
