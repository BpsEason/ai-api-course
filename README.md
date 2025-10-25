# AI API 教學模組

**從零到一，學會建構 5 個生產級 AI API + Docker 部署 + MLOps 實踐**

> **適合對象**：  
> - 想轉職 AI 後端工程師的 Python 開發者  
> - 正在準備技術面試 / 作品集的工程師  
> - 企業內訓、學校課程、技術共學團的講師與學員  
> - 想用 FastAPI 快速落地 AI 產品的創業團隊

---

## 教學目標（學完你會獲得）

| 技能 | 實踐內容 |
|------|----------|
| FastAPI 模組化架構 | `routers` / `schemas` / `models` 三層分離 |
| 模型推論與訓練分離 | `joblib` + 預訓練 + 容器化 |
| Hugging Face 整合 | `pipeline` + 情緒分析 |
| RAG 系統實作 | `sentence-transformers` + `faiss` |
| 外部 LLM 串接 | OpenAI SDK + Token 追蹤 |
| Docker 多階段建置 | 輕量映像 + 模型預載 |
| MLOps 思維 | 環境變數、測試、驗收、部署 |

> **成果**：一份可部署、可展示、可擴充的 AI API 作品集！

---

## 專案架構（一目了然）

```bash
ai-api-course/
├── app/
│   ├── models/          # 模型邏輯（RAG、房價、NLP）
│   ├── routers/         # 5 個 API 路由
│   ├── schemas/         # Pydantic 輸入輸出驗證
│   ├── utils/           # 共用工具（logger）
│   └── main.py          # FastAPI 入口
├── data/                # RAG 知識庫（可編輯）
├── tests/               # 5 個 pytest 單元測試
├── Dockerfile           # 多階段建置
├── docker-compose.yml   # 一鍵啟動
├── verify.py            # 一鍵驗收腳本
└── README.md            # 你正在看的這份！
```

---

## 快速啟動（3 步驟，零安裝）

### 1. 複製專案
```bash
git clone https://github.com/BpsEason/ai-api-course.git
cd ai-api-course
```

### 2. 設定環境變數
```bash
cp .env.example .env
```
編輯 `.env` 填入你的 OpenAI Key：
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

### 3. 一鍵啟動（Docker）
```bash
docker-compose up --build -d
```

> **成功訊息**：`ai_api_service | INFO:     Uvicorn running on http://0.0.0.0:8000`

---

## 存取與驗證

| 功能 | 指令 |
|------|------|
| API 文件 | [http://localhost:8000/docs](http://localhost:8000/docs) |
| 健康檢查 | `curl http://localhost:8000/` |
| 驗收腳本 | `python verify.py` |

---

## 5 個 API 功能一覽

| 版本 | 功能 | 路徑 | 輸入範例 |
|------|------|------|----------|
| `/v1/sentiment` | 情緒分析 | `POST /predict` | `{"text": "I love AI!"}` |
| `/v2/house` | 房價預測 | `POST /predict` | `{"size": 1200, "rooms": 3}` |
| `/v3/chat` | ChatGPT 對話 | `POST /chat` | `{"text": "你好"}` |
| `/v4/rag` | RAG 問答 | `POST /ask` | `{"text": "退款政策？"}` |
| `/v5/analyze` | 情緒 + 關鍵字 | `POST /analyze` | `{"text": "FastAPI 超強！"}` |

> **試試看**：
```bash
curl -X POST http://localhost:8000/v1/sentiment/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this course!"}'
```

---

## 教學重點解析（每段程式碼都有目的）

### 1. **FastAPI 模組化設計**
- `include_router(prefix="/v1/...")` → 版本控制
- `Pydantic Field(..., max_length=500)` → 防 DoS 攻擊

### 2. **Docker 多階段建置（MLOps 核心）**
```dockerfile
FROM ... as builder          # 建置階段：下載模型、訓練
FROM python:3.11-slim        # 執行階段：僅保留必要檔案
```
> 好處：映像檔 < 800MB，啟動 < 3 秒

### 3. **模型預訓練（避免冷啟動）**
```dockerfile
RUN python -c "from app.models.house_price import train_and_save_model; ..."
```
> 模型已內建於映像檔，API 啟動即用

### 4. **RAG 動態知識庫**
- 編輯 `data/documents.txt` → 即時更新問答內容
- `volumes` 掛載 → 容器外可編輯

---

## 延伸練習（挑戰自己）

| 等級 | 挑戰任務 |
|------|----------|
| 1星 | 修改 `data/documents.txt`，加入公司政策 |
| 2星 | 將房價模型改為 `RandomForest` |
| 3星 | 加入 `Redis` 快取 RAG 查詢 |
| 4星 | 加上 `Streamlit` 前端介面 |
| 5星 | 部署到 Railway + 加上 GitHub Actions CI |

---

## 部署建議（一鍵上雲）

| 平台 | 指令 |
|------|------|
| **Railway** | `railway up` |
| **Render** | 連結 GitHub → 自動部署 |
| **Vercel** | 搭配 `vercel.json` |

> **免費方案即可運行**！

---

## 測試與驗收

```bash
# 執行所有測試
pytest -v

# 一鍵驗收
python verify.py
```

**預期輸出**：
```
5 passed
All tests passed!
API /v1/sentiment/predict: 200 -> {'label': 'POSITIVE', 'score': 0.99}
```

---

## 參考資源

| 類型 | 連結 |
|------|------|
| FastAPI 官方 | https://fastapi.tiangolo.com |
| Hugging Face | https://huggingface.co/models |
| Docker 最佳實踐 | https://docs.docker.com/develop/develop-images/multistage-build/ |
| RAG 入門 | https://www.pinecone.io/learn/retrieval-augmented-generation/ |

---

## 常見問題（FAQ）

**Q：沒有 GPU 也能跑嗎？**  
A：完全可以！所有模型都在 CPU 上運行（`faiss-cpu`、`torch` CPU 版）

**Q：可以不用 Docker 嗎？**  
A：可以！但建議用 Docker 確保環境一致性。

**Q：如何更新 RAG 知識庫？**  
A：直接編輯 `data/documents.txt`，重啟容器即可。

---

## 貢獻與回饋

歡迎提交 PR 或 Issue！  
讓我們一起把這份教學模組變成 **業界最強的 AI API 入門範本**！

---

**Made with ❤️ by AI Course Team**  
`v3.0 | 2025-10-25`
```

