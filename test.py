from fastapi import FastAPI

API_PATH = "/api"

# create the main app that only serves static files at root
app = FastAPI(docs_url=None, redoc_url=None)

# create the api
api = FastAPI(root_path=API_PATH, docs_url="/docs")


# -- demo urls
@api.get("/books")
async def books():
    pass


# mount the api on subpath
app.mount(API_PATH, api, "api")
