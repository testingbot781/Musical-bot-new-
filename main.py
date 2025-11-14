from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN
import os

app = Client(
    "bot_session",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# -------------------------- COMMANDS -----------------------------

@app.on_message(filters.command("start"))
async def start_cmd(_, message: Message):
    await message.reply_text(
        "👋 Welcome!\n\n"
        "Send any song name to download MP3.\n"
        "Use /help to see all commands."
    )

@app.on_message(filters.command("help"))
async def help_cmd(_, message: Message):
    await message.reply_text(
        "📘 **Available Commands**\n\n"
        "🎵 Send any **song name** to get MP3\n"
        "📄 /file <filename> – Get file from channel\n"
        "➕ /add <user_id> <days> – Add premium\n"
        "➖ /rem <user_id> – Remove premium\n"
        "📢 /broadcast <message> – Broadcast message\n"
    )

@app.on_message(filters.command("file"))
async def get_file(_, message: Message):
    try:
        query = message.text.split(" ", 1)[1]
    except:
        return await message.reply("❗ Format: `/file filename`")

    await message.reply(f"📂 Searching file: `{query}` (feature placeholder)")

@app.on_message(filters.command("add"))
async def add_premium(_, message: Message):
    await message.reply("⭐ Premium Added (demo placeholder)")

@app.on_message(filters.command("rem"))
async def remove_premium(_, message: Message):
    await message.reply("❌ Premium Removed (demo placeholder)")

@app.on_message(filters.command("broadcast"))
async def broadcast_msg(_, message: Message):
    await message.reply("📢 Broadcast sent (demo placeholder)")

# -------------------------- SONG SEARCH -----------------------------

@app.on_message(filters.text & ~filters.command([]))
async def song_handler(_, message: Message):
    query = message.text

    # Placeholder for audio download logic
    await message.reply(f"🎶 Searching YouTube: `{query}`\n(This is a placeholder)")

# --------------------------------------------------------------------

print("Bot Started...")
app.run()
