import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
from pathlib import Path

MODEL_PATH = Path("app/models/house_price_model.joblib")

def train_and_save_model():
    # 範例數據：[大小, 房間數] -> 價格
    X = np.array([[500, 1], [800, 2], [1200, 3], [1500, 4], [2000, 5]])
    y = np.array([150000, 220000, 320000, 400000, 520000])
    model = LinearRegression()
    model.fit(X, y)
    MODEL_PATH.parent.mkdir(exist_ok=True)
    # 實踐：使用 joblib 儲存訓練好的模型二進制檔
    joblib.dump(model, MODEL_PATH)
    print(f"Model trained and saved to {MODEL_PATH}")

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Model not found. Run training first.")
    return joblib.load(MODEL_PATH)
