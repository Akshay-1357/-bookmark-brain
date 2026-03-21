from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from searcher import search_pages
from embedder import store_page as embed_store_page
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class PageData(BaseModel):
    url : str
    title : str
    content :str



@app.post("/store")
def store(data: PageData):
    embed_store_page(data.url, data.title, data.content)
    return {"status": "ok"}
    

@app.get("/search")
def search(query: str):
    results = search_pages(query)
    return {"metadatas": [results]}
