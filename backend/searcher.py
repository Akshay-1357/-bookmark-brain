import chromadb

from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="chroma_store")
collection = client.get_or_create_collection("pages")
model = SentenceTransformer("all-MiniLM-L6-v2")

def search_pages(query , n_results = 5):
    embedding = model.encode(query).tolist()
    return collection.query(
        query_embeddings = [embedding], 
        n_results=n_results,
          include=["metadatas", "distances"]
          )