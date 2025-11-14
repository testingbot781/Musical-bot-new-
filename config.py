import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# -----------------------------------------
# REQUIRED VARIABLES (These MUST be in .env)
# -----------------------------------------
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# -----------------------------------------
# OPTIONAL VARIABLES (Add in .env only if needed)
# -----------------------------------------
OWNER_ID = os.getenv("OWNER_ID")
if OWNER_ID:
    OWNER_ID = int(OWNER_ID)

MONGO_URL = os.getenv("MONGO_URL", None)
LOG_CHANNEL = os.getenv("LOG_CHANNEL", None)
