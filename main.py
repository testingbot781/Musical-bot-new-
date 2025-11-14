from flask import Flask, request
from pyrogram import Client, filters
import os
import threading

# Load ENV
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Flask App
app = Flask(__name__)

# Pyrogram Bot Client
bot = Client(
    "mybot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# Start Bot in background thread (important for Render)
def run_bot():
    bot.run()

threading.Thread(target=run_bot).start()


# ---------- WEBHOOK ENDPOINT ----------
@app.post(f"/{BOT_TOKEN}")
def webhook():
    update = request.get_json()
    if update:
        bot.process_updates([update])
    return "OK", 200


# ---------- HOME PAGE ----------
@app.get("/")
def home():
    return "Bot is running on Render!", 200


# ---------- BOT HANDLERS ----------
@bot.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply("Hello! Your webhook bot is working successfully.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
