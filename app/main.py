from fastapi import FastAPI
from app.routers import sentiment, house, chat, rag, analyze

# 實踐：定義 API 標題和版本
app = FastAPI(title="AI API Portfolio v3.0 (Dockerized)", version="3.0.0")

# 實踐：透過 include_router 載入模組，並使用 prefix 進行版本控制 (API 版本化)
app.include_router(sentiment.router, prefix="/v1/sentiment")
app.include_router(house.router, prefix="/v2/house")
app.include_router(chat.router, prefix="/v3/chat")
app.include_router(rag.router, prefix="/v4/rag")
app.include_router(analyze.router, prefix="/v5/analyze")

@app.get("/")
async def root():
    # 實踐：根目錄導向文件
    return {"message": "AI API Portfolio v3.0 (Dockerized)", "docs": "/docs"}
