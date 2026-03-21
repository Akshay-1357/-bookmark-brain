from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from embedder import store_page
from searcher import search_pages
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
def store_page_endpoint(data: PageData):
    return store_page(data.url, data.title, data.content)
    
    
@app.get("/search")
def search(query:str):
    return search_pages(query , n_results = 5)
