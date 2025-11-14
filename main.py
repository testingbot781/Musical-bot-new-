import os
from flask import Flask, request
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

# Flask App
app_server = Flask(__name__)

# Pyrogram Bot (Webhook Mode)
tg_bot = Client(
    "webhook_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=1,
    in_memory=True
)

# ----------------- Bot Commands -----------------

@tg_bot.on_message(filters.command("start"))
async def start_handler(_, message):
    await message.reply(
        "👋 Welcome!\n\n"
        "Send any song name to download MP3.\n"
        "Use /help to see all commands."
    )

@tg_bot.on_message(filters.command("help"))
async def help_handler(_, message):
    await message.reply(
        "📘 **Commands**\n\n"
        "🎵 Send any song name\n"
        "📂 /file <name>\n"
        "⭐ /add <user_id> <days>\n"
        "❌ /rem <user_id>\n"
        "📢 /broadcast <msg>"
    )

@tg_bot.on_message(filters.text & ~filters.command(["start", "help"]))
async def song_handler(_, message):
    query = message.text
    await message.reply(f"🎶 Searching: `{query}` (demo placeholder)")

# ----------------- Webhook -----------------

@app_server.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json()
    tg_bot.process_update(update)
    return "OK", 200

@app_server.route("/")
def home():
    return "Bot is running on Render (Webhook Mode)."

# ----------------- Main -----------------

if __name__ == "__main__":
    print("Starting Webhook Bot...")
    tg_bot.start()
    port = int(os.environ.get("PORT", 10000))
    app_server.run(host="0.0.0.0", port=port)
