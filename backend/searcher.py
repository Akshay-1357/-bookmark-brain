
import os
from dotenv import load_dotenv
from supabase import create_client
from sentence_transformers import SentenceTransformer

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
model = SentenceTransformer("all-MiniLM-L6-v2")


def search_pages(query, n_results=5):
   
    embedding = model.encode(query).tolist()

    response = supabase.rpc("match_pages", {
        "query_embedding": embedding,
        "match_count": n_results
    }).execute()

   
    return response.data