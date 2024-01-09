import os
import redis
from .base import DbItem

database_uri = os.environ.get("DATABASE_URI")


class Database:
    def __init__(self, conn):
        self.redis = conn
        self.books = DbItem(conn, prefix="book")

    def close(self):
        self.redis.close()


# Dependency
def get_database():
    conn = redis.from_url(database_uri)
    return Database(conn=conn)


async def get_db():
    db = get_database()

    try:
        yield db
    finally:
        db.close()
