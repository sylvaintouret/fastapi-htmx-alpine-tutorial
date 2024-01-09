import json

from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from database import get_db, Database, get_database


class BookRead(BaseModel):
    title: str
    pageCount: int
    authors: list[str]
    thumbnailUrl: str | None = None
    shortDescription: str | None = None
    id: str
    isbn: str


API_PATH = "/api"

# create the main app that only serves static files at root
app = FastAPI(docs_url=None, redoc_url=None)

# create the api
api = FastAPI(root_path=API_PATH, docs_url="/docs")


@app.on_event("startup")
async def startup_event():
    db = get_database()
    with open("books.json", "r", encoding="utf-8") as f:
        datas = json.load(f)

    for data in datas.get("books", []):
        db.books.add(data)


# -- demo urls
@api.get("/books", response_model=list[BookRead])
async def books(db=Depends(get_db)):
    return db.books.all()


@api.get("/book/{uid}", response_model=BookRead)
async def book_get(uid: str, db=Depends(get_db)):
    return db.books.get(uid)


# mount the api on subpath
app.mount(API_PATH, api, "api")

app.mount("/", StaticFiles(directory="static", html=True), name="static")
