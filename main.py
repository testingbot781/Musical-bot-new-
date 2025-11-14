import os
import json
from flask import Flask, request
from pyrogram import Client, filters
import threading

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ---------------- BOT CLIENT ---------------- #
bot = Client(
    "webhook_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# Run bot in background thread
def start_pyrogram():
    bot.start()

threading.Thread(target=start_pyrogram).start()

# ---------------- FLASK APP ---------------- #
app = Flask(__name__)

@app.get("/")
def home():
    return "Bot running with webhook!", 200


# Webhook route (MUST match telegram webhook url)
@app.post(f"/{BOT_TOKEN}")
def webhook_endpoint():
    try:
        data = request.get_json()

        if data:
            bot.process_update(data)

        return "OK", 200
    except Exception as e:
        return str(e), 500


# ----- BOT COMMAND ------ #
@bot.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply("Webhook connected successfully! Bot is active ✔")


# -------------- RUN FLASK -------------- #
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
