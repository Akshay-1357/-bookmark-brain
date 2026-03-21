import chromadb
from sentence_transformers import SentenceTransformer
import uuid
import re

client = chromadb.PersistentClient(path="chroma_store")
collection = client.get_or_create_collection("pages")
model = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_text(text, chunk_size=500, overlap=50):
    
    text = re.sub(r'\s+', ' ', text).strip()
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks

def store_page(url, title, text):

    chunks = chunk_text(text)
  
    for chunk in chunks:
   

        embedding = model.encode(chunk).tolist()
        
        collection.add(
      

            ids=[str(uuid.uuid4())],
 
            embeddings=[embedding],
           
            metadatas=[{"url": url, "title": title, "chunk": chunk}]
            
        )
    