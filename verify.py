import subprocess, requests
def run_tests():
    print("--- Running Pytest Unit Tests ---")
    # 實踐：使用 subprocess 運行測試
    result = subprocess.run(["pytest", "-q"], capture_output=True, text=True)
    print(result.stdout)
    return "5 passed" in result.stdout

def check_api():
    print("\n--- Checking API Health ---")
    try:
        # 實踐：檢查第一個 API 端點 (通常為最穩定的)
        r = requests.post("http://localhost:8000/v1/sentiment/predict", json={"text": "Hi"}, timeout=10)
        print(f"API /v1/sentiment/predict: Status {r.status_code} -> {r.json()}")
    except: 
        print("API Check FAILED: Start server first (e.g. use 'docker-compose up')!")
        
if __name__ == "__main__":
    print("Verifying Project v3.0...")
    if run_tests(): 
        print("\n✅ All tests passed!")
        check_api()
    else: 
        print("\n❌ Tests failed!")
        check_api()
