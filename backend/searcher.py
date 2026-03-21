
import os
from dotenv import load_dotenv
from supabase import create_client
from fastembed import TextEmbedding

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

model = TextEmbedding("BAAI/bge-small-en-v1.5")


def search_pages(query, n_results=5):
   
    embedding = list(model.embed([query]))[0].tolist()

    response = supabase.rpc("match_pages", {
        "query_embedding": embedding,
        "match_count": n_results
    }).execute()

   
    return response.data