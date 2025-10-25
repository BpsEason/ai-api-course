from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from pathlib import Path

class RAGSystem:
    def __init__(self, docs_path="data/documents.txt"):
        # Embedding 模型：將文字轉換為向量
        self.model = SentenceTransformer('all-MiniLM-L6-v2') 
        self.index = None
        self.documents = []
        self.dimension = 384
        self.load_documents(docs_path)
    
    def load_documents(self, path: str):
        file = Path(path)
        if not file.exists():
            docs = ["No documents available. Default data used."]
        else:
            # 實踐：從外部文件載入知識庫內容
            docs = [line.strip() for line in file.read_text().splitlines() if line.strip()]
        
        if not docs:
            docs = ["No documents available. Default data used."]
            
        # 實踐：將文件向量化
        embeddings = self.model.encode(docs)
        # 實踐：建立 Faiss 索引 (L2 距離)
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(embeddings.astype('float32'))
        self.documents = docs
    
    def query(self, question: str, k: int = 1):
        if not self.documents or self.documents == ["No documents available. Default data used."]: return "Knowledge base is empty. Please check data/documents.txt"
        q_emb = self.model.encode([question]).astype('float32')
        # 實踐：在 Faiss 索引中搜索最相似的文件
        D, I = self.index.search(q_emb, k)
        return self.documents[I[0][0]] # 返回最相似的一段文字

rag = RAGSystem()
