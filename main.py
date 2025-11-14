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
    workdir="./"
)

# ----------- START BOT IN BACKGROUND ----------- #
def start_bot():
    bot.run()

threading.Thread(target=start_bot).start()


# ----------------- FLASK APP ------------------ #
app = Flask(__name__)

@app.get("/")
def home():
    return "Bot is online and webhook is active!", 200


# ------------- WEBHOOK RECEIVER --------------- #
@app.post(f"/webhook/{BOT_TOKEN}")
def webhook():
    try:
        update = request.get_json()

        if update:
            bot.dispatcher.updates_queue.put(update)

        return "OK", 200

    except Exception as e:
        return str(e), 500


# -------- BOT COMMAND HANDLER -------- #
@bot.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("Webhook bot is working successfully!")


# ---------------- RUN FLASK ------------------ #
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
