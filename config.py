import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))
OWNER_USERNAME = os.getenv("OWNER_USERNAME")
CHANNEL_ID = os.getenv("CHANNEL_ID")
YT_API_KEY = os.getenv("YT_API_KEY")
TELEGRAM_HASH = os.getenv("TELEGRAM_HASH")
MONGO_URL = os.getenv("MONGO_URL")
