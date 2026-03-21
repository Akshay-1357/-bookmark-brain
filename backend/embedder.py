
import os
from dotenv import load_dotenv
from supabase import create_client
from fastembed import TextEmbedding
import re
import uuid


load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
model = TextEmbedding("BAAI/bge-small-en-v1.5")


def chunk_text(text, chunk_size=500, overlap=50):
    
    text = re.sub(r'\s+', ' ', text).strip()
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks


def store_page(url, title, text):
    chunks = chunk_text(text)

    for chunk in chunks:
      
        embedding = list(model.embed([chunk]))[0].tolist()

        supabase.table("pages").insert({
            "url": url,
            "title": title,
            "chunk": chunk,
            "embedding": embedding
        }).execute()

    return {"status": "ok", "chunks_stored": len(chunks)}