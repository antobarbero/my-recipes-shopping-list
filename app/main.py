from fastapi import FastAPI
from .routers import recipes

app = FastAPI()

app.include_router(recipes.router)


@app.get("/")
def read_root():
    return "Welcome to the recipes web api."
