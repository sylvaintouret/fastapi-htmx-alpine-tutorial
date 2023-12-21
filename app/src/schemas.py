from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BookBase(BaseModel):
    title: str
    pages: int
    author: str
    subtitle: Optional[str]
    published: datetime
    publisher: Optional[str]
    description: Optional[str]
    website: Optional[str]


class BookRead(BookBase):
    isbn: str


class BookUpdate(BookBase):
    isbn: str


class BookAdd(BookBase):
    pass
