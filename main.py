import os
from flask import Flask, request
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

# Flask Server
app_server = Flask(__name__)

# Pyrogram Bot
tg_bot = Client(
    "render_webhook_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=1,
    in_memory=True
)

# ------------------- Commands -------------------

@tg_bot.on_message(filters.command("start"))
async def start_handler(_, message):
    await message.reply(
        "👋 Welcome!\n"
        "Send any song name to download MP3.\n"
        "Use /help to see more commands."
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
    await message.reply(f"🎶 Searching: `{message.text}` (demo placeholder)")

# ------------------- Webhook Route -------------------

@app_server.route(f"/webhook/{BOT_TOKEN}", methods=["POST"])
def webhook():
    try:
        tg_bot.process_update(request.get_json(force=True))
    except Exception as e:
        print("Error:", e)
    return "OK", 200

@app_server.route("/")
def home():
    return "Bot Running Successfully (Webhook Mode)"

# ------------------- Run -------------------

if __name__ == "__main__":
    print("Starting Bot in Webhook Mode...")
    tg_bot.start()
    port = int(os.environ.get("PORT", 10000))
    app_server.run(host="0.0.0.0", port=port)
