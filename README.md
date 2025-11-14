🚀 Telegram Multi-Feature Bot

A clean, fast and stable Telegram bot built using **Pyrogram**.  
Simple setup, easy deployment, and fully ready for Render hosting.

Made with ❤️ by **@technicalserena**

---

## 📌 Requirements (ENV Variables)

Render / Local — same variables required:

API_ID=your_api_id API_HASH=your_api_hash BOT_TOKEN=your_bot_token OWNER_ID=your_telegram_id   # optional MONGO_URL=your_mongodb_url  # optional LOG_CHANNEL=channel_id      # optional

---

## 📦 Installation (Local)

```bash
git clone https://github.com/yourusername/yourrepo
cd yourrepo
pip install -r requirements.txt
python3 main.py


---

🌐 Render Deployment Guide

1️⃣ Create New Web Service
Select your GitHub repository.

2️⃣ Build Command

pip install -r requirements.txt

3️⃣ Start Command

python3 main.py

4️⃣ Add Environment Variables exactly as listed above.

5️⃣ Deploy
Render automatically starts your bot.


---

🎮 Bot Commands (BotFather Format — Copy/Paste Ready)

start - 🚀 Start the bot
help - 📘 Show help menu
about - 🧿 About this bot

batch - 🗂️ Process multiple links at once
single - 🔗 Process single link
login - 🔑 Login to your account
logout - 🚪 Logout from your account

yt - 🎬 Download YouTube videos
song - 🎵 Download audio from YouTube

status - 📊 View bot status
setbot - 🛠️ Set your own bot
adl - 🎧 Download audio (30+ sites)
dl - 📥 Download videos (30+ sites)

transfer - 🎁 Gift premium to others
info - 🪪 Get user information
broadcast - 📢 Send message to all users
id - 🆔 Get chat/user ID


---

📝 Usage Guide

💠 Start

Send:

/start

Bot will show welcome panel.

💠 Process a YouTube Video

/single https://youtube.com/.....

💠 Bulk Processing

/batch

Upload your file containing multiple links.

💠 Login

/login

💠 Logout

/logout

💠 Check Status

/status


---

📁 Project Files

main.py
config.py
requirements.txt
README.md
modules/
handlers/


---

👑 Credits

Developed by @technicalserena
Please give proper credit if you use this project.


---

🛡 License

This project is free to modify and use.

---
