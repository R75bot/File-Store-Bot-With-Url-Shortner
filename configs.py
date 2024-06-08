import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "26563318"))
  API_HASH = os.environ.get("API_HASH", "0c56c2a16ea879f707bcfe077c4067f4")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7334813604:AAHpzyBliUKT8mWd-3SLyRTL9YyP9yo7YRI")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "FileSpot_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002085214143"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "publicearn.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "c4527d03c7519c169a0c878aca3c0d048e070de2")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "7052947046"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://illegalbea:biteherepublic@cluster0.icclskc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002085214143")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002010583674"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [VJ](https://telegram.me/Made_in_Agra)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Made_in_Agra)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
