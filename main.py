from fastapi import FastAPI
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus
from routes.routes import router

app = FastAPI()

app.include_router(router)