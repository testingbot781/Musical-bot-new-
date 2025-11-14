import os
from dotenv import load_dotenv

load_dotenv()

# Required
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Optional
OWNER_ID = os.getenv("OWNER_ID")
if OWNER_ID:
    OWNER_ID = int(OWNER_ID)

MONGO_URL = os.getenv("MONGO_URL", None)
LOG_CHANNEL = os.getenv("LOG_CHANNEL", None)
