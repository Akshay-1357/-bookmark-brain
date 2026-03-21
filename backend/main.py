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
def store_page(data: PageData):
    return {"status": "ok"}
    

@app.get("/search")
def search(query : str):
    return { "results":[]}
