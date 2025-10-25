from transformers import pipeline
import spacy
from typing import List

class NLPAnalyzer:
    def __init__(self):
        # 任務 1: 情緒分析
        self.sentiment = pipeline("sentiment-analysis")
        try:
            # 任務 2: 關鍵字抽取 (使用 spaCy 進行詞性標註)
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            # MLOps 實踐：如果模型找不到，直接拋錯。Docker 應確保預載
            raise RuntimeError("spaCy model 'en_core_web_sm' not found. Check Dockerfile.")
    
    def analyze(self, text: str):
        # 情緒分析
        sent = self.sentiment(text)[0]
        sentiment = sent['label'].lower()
        
        # 關鍵字抽取
        doc = self.nlp(text)
        # 實踐：抽取所有名詞 (NOUN) 和專有名詞 (PROPN) 作為關鍵字
        keywords = [token.text.lower() for token in doc if token.pos_ in ['NOUN', 'PROPN']]
        # 實踐：去重並限制數量
        return {"sentiment": sentiment, "keywords": list(set(keywords))[:5]}

analyzer = NLPAnalyzer()
