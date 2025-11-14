import os
import json
from flask import Flask, request
from pyrogram import Client, filters
from pyrogram.types import Update
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


# Background thread for pyrogram
def start_bot():
    bot.start()

threading.Thread(target=start_bot).start()


# ---------------- FLASK APP ---------------- #
app = Flask(__name__)

@app.get("/")
def home():
    return "Telegram Music Bot Running via Webhook", 200


# ---------- EXACT SAME ROUTE AS WEBHOOK ---------- #
@app.post(f"/{BOT_TOKEN}")
def webhook():
    try:
        data = request.get_json()

        if not data:
            return "No data", 400

        # Convert raw JSON to Telegram Update
        update = Update.de_json(data, bot)

        # Pass update to pyrogram
        bot.process_update(update)

        return "OK", 200

    except Exception as e:
        return f"Error: {str(e)}", 500


# ---------------- BOT COMMAND ---------------- #
@bot.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("Bot is active via webhook! Send any message to test.")


# -------------------- RUN -------------------- #
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
