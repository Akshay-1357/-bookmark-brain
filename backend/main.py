from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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
