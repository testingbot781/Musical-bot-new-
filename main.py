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
    "webhook_mode",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ----------- START BOT IN BACKGROUND ----------- #
def run_bot():
    bot.run()

threading.Thread(target=run_bot).start()


# ----------------- FLASK APP ------------------ #
app = Flask(__name__)

@app.get("/")
def home():
    return "Bot Running + Webhook Active", 200


# ------------- EXACT MATCHING ROUTE --------------- #
@app.post(f"/{BOT_TOKEN}")
def handle_update():
    try:
        update = request.get_json()

        if update:
            # Pyrogram queue
            bot.dispatcher.updates_queue.put(update)

        return "OK", 200

    except Exception as e:
        return str(e), 500


# -------- BOT COMMAND HANDLER -------- #
@bot.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply("Webhook successfully connected! Bot is alive.")


# ---------------- RUN FLASK ------------------ #
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
