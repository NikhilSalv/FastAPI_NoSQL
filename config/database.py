from pymongo import MongoClient
from urllib.parse import quote_plus

username = "nikhilsalvi1207"
password = quote_plus("Nikhil@123") 
client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.ry9ynfd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.todo_db

collection_name = db["todo_collection"]