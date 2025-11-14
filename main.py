from pyrogram import Client, filters
from config import *
from database import *
from utils import yt_search, download_mp3
import os

app = Client(
    "SongBot",
    bot_token=BOT_TOKEN,
    api_id=12345,
    api_hash=TELEGRAM_HASH
)


# ---------------------- Start ----------------------
@app.on_message(filters.command("start"))
async def start(_, msg):
    add_user(msg.from_user.id)

    await msg.reply(
        "**Welcome to Song Search Bot 🎵**\n\n"
        "Use /help for full command list."
    )


# ---------------------- Help ----------------------
@app.on_message(filters.command("help"))
async def help(_, msg):
    await msg.reply(
        "**Available Commands**\n\n"
        "/help — Show help\n"
        "[Song Name] — Get MP3 via YouTube\n"
        "/file <name> — Get file from channel\n"
        "/add <user> <days> — Add premium\n"
        "/rem <user> — Remove premium\n"
        "/broadcast <msg> — Broadcast to all users\n"
    )


# ---------------------- Search Song ----------------------
@app.on_message(filters.text & ~filters.command(["file", "add", "rem", "broadcast"]))
async def song(_, msg):
    user_id = msg.from_user.id

    if not is_premium(user_id):
        return await msg.reply("You need **premium** to use song search.")

    query = msg.text

    data = yt_search(query, YT_API_KEY)
    if not data:
        return await msg.reply("No results found.")

    await msg.reply("Downloading...")

    mp3 = download_mp3(data["video_id"])
    if not mp3:
        return await msg.reply("Download failed.")

    await msg.reply_document(mp3, caption=data["title"])
    os.remove(mp3)


# ---------------------- File Fetch ----------------------
@app.on_message(filters.command("file"))
async def file_send(_, msg):
    if len(msg.command) < 2:
        return await msg.reply("Usage: /file filename.ext")

    filename = msg.text.split(" ", 1)[1]

    try:
        await msg.reply("Fetching file...")
        await msg.reply_document(
            CHANNEL_ID,
            file_name=filename
        )
    except Exception:
        await msg.reply("File not found in channel.")


# ---------------- Owner Commands ----------------

@app.on_message(filters.command("add"))
async def add_premium_cmd(_, msg):
    if msg.from_user.id != OWNER_ID:
        return

    try:
        uid = int(msg.command[1])
        days = int(msg.command[2])
        set_premium(uid, days)
        await msg.reply(f"Premium added for {uid} for {days} days.")
    except:
        await msg.reply("Format: /add user days")


@app.on_message(filters.command("rem"))
async def remove_premium_cmd(_, msg):
    if msg.from_user.id != OWNER_ID:
        return

    try:
        uid = int(msg.command[1])
        remove_premium(uid)
        await msg.reply(f"Premium removed from {uid}.")
    except:
        await msg.reply("Format: /rem user")


@app.on_message(filters.command("broadcast"))
async def broadcast(_, msg):
    if msg.from_user.id != OWNER_ID:
        return

    text = msg.text.replace("/broadcast", "").strip()
    if not text:
        return await msg.reply("Usage: /broadcast message")

    for u in get_all_users():
        try:
            await app.send_message(u, text)
        except:
            pass

    await msg.reply("Broadcast sent.")


print("Bot Started...")
app.run()
