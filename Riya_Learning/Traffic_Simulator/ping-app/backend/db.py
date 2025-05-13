from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client["ping_app"]
collection = db["ping_results"]

def insert_ping(record):
    collection.insert_one(record)

def fetch_history(query):
    return list(collection.find(query, {"_id": 0}))
