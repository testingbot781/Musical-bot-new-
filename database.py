from pymongo import MongoClient
from datetime import datetime, timedelta
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client["song_bot"]
users = db["users"]

def add_user(user_id):
    if not users.find_one({"user_id": user_id}):
        users.insert_one({"user_id": user_id, "premium": False, "expiry": None})

def set_premium(user_id, days):
    expiry = datetime.now() + timedelta(days=days)
    users.update_one(
        {"user_id": user_id},
        {"$set": {"premium": True, "expiry": expiry}}
    )

def remove_premium(user_id):
    users.update_one(
        {"user_id": user_id},
        {"$set": {"premium": False, "expiry": None}}
    )

def is_premium(user_id):
    data = users.find_one({"user_id": user_id})
    if not data:
        return False
    if not data.get("premium"):
        return False
    if data.get("expiry") and data["expiry"] < datetime.now():
        remove_premium(user_id)
        return False
    return True

def get_all_users():
    return [u["user_id"] for u in users.find({})]
