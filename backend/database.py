import os
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Defaults to localhost if .env is missing
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

class MongoHandler:
    def __init__(self):
        try:
            self.client = MongoClient(MONGO_URI)
            self.db = self.client["FinSent_Battle_Arena"]
            self.collection = self.db["logs"]
            # Test connection
            self.client.admin.command('ping')
            print("✅ MongoDB Connected")
        except Exception as e:
            print(f"⚠️ MongoDB Failed: {e}")
            self.collection = None

    def log_battle(self, data: dict):
        """Logs the result of the model comparison"""
        if self.collection is not None:
            entry = { "timestamp": datetime.utcnow(), **data }
            try:
                self.collection.insert_one(entry)
            except Exception as e:
                print(f"DB Log Error: {e}")

    def fetch_recent_logs(self, limit=5):
        """Fetches the latest disagreement logs for the dashboard"""
        if self.collection is not None:
            return list(self.collection.find({}, {"_id": 0}).sort("timestamp", -1).limit(limit))
        return []