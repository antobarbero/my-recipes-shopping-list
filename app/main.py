from fastapi import FastAPI
from .routers import recipes
from pymongo.mongo_client import MongoClient
from .config import settings
import logging


app = FastAPI()

logger = logging.getLogger("uvicorn.error")

app.include_router(recipes.router)


@app.get("/")
def read_root():
    return "Welcome to the recipes web api."


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(settings.mongo_db_connection_string)
    app.database = app.mongodb_client[settings.db_name]
    logger.info("Connected to the MongoDB database!")


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
    logger.info("MongoDB connection closed.")
