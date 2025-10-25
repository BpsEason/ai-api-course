# === 階段 1: Build & 模型下載 (Builder) ===
FROM python:3.11-slim as builder

# 設定環境變數
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY requirements.txt .
COPY app app
COPY data data

# 1. 安裝 Python 依賴
RUN pip install --no-cache-dir -r requirements.txt

# 2. 預先下載所有大型模型 (節省 runtime 啟動時間)
RUN echo "Downloading Hugging Face and spaCy models..."
RUN python -c "from transformers import pipeline; pipeline('sentiment-analysis', model='cardiffnlp/twitter-roberta-base-sentiment-latest')"
RUN python -c "import spacy; spacy.cli.download('en_core_web_sm')"

# 3. 訓練 House Price 模型並保存 (確保模型存在於 Image)
RUN python -c "from app.models.house_price import train_and_save_model; train_and_save_model()"

# === 階段 2: Final Runtime 映像檔 ===
FROM python:3.11-slim

# 設定環境變數
ENV PYTHONUNBUFFERED 1
ENV PORT 8000
ENV TZ Asia/Taipei

# 複製程式碼與運行環境
WORKDIR /usr/src/app
# 複製 site-packages 避免重新安裝
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/src/app .

# 啟動命令 (生產環境通常使用 Gunicorn + Uvicorn Worker)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
