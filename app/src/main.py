from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import json
from pydantic import BaseModel, Field
from typing import List, Optional


class BookRead(BaseModel):
    title: str
    pageCount: int
    authors: list[str]
    thumbnailUrl: Optional[str] = None
    shortDescription: Optional[str] = None
    id: int = Field(..., alias="_id")
    isbn: str


API_PATH = "/api"

# create the main app that only serves static files at root
app = FastAPI(docs_url=None, redoc_url=None)

# create the api
api = FastAPI(root_path=API_PATH, docs_url="/docs")


# -- demo urls
@api.get("/books", response_model=List[BookRead])
async def books():
    with open("books.json", "r") as f:
        data = json.load(f)
    return data.get("books", [])


# mount the api on subpath
app.mount(API_PATH, api, "api")

app.mount("/", StaticFiles(directory="static", html=True), name="static")
