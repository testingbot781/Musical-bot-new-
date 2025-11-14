import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

OWNER_ID = os.getenv("OWNER_ID")
if OWNER_ID:
    OWNER_ID = int(OWNER_ID)
