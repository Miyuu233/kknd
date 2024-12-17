from telethon import TelegramClient
from telethon.tl.types import UserStatusOnline, UserStatusOffline
from datetime import datetime, timezone, timedelta
import asyncio
import requests

API_ID = 
API_HASH = ''
BOT_TOKEN = ""
USERNAMES = ['User1', 'User2', 'User3']
BOT_CHAT_ID = ''

client = TelegramClient('kknd', API_ID, API_HASH)

def send_bot_message(chat_id, message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(f"[ERROR] Failed to send message: {response.text}")

def get_cst_time():
    utc_now = datetime.now(timezone.utc)
    cst_now = utc_now + timedelta(hours=8)
    return cst_now.strftime("%Y-%m-%d %H:%M:%S")

async def monitor_users_status():
    previous_statuses = {username: None for username in USERNAMES}

    async with client:
        while True:
            for username in USERNAMES:
                try:         
                    user = await client.get_entity(username)
                    status = user.status

                    if isinstance(status, UserStatusOnline):
                        current_status = "Online"
                    elif isinstance(status, UserStatusOffline):
                        current_status = "Offline"
                    else:
                        current_status = "Unknown"

                    if current_status != previous_statuses[username]:
                        previous_statuses[username] = current_status
                        cst_time = get_cst_time()
                        message = f"[{cst_time}] @{username} {current_status}."
                        send_bot_message(BOT_CHAT_ID, message)
                        print(f"[INFO] Notification sent: {message}")

                except Exception as e:
                    print(f"[ERROR] Failed to monitor @{username}: {e}")

            await asyncio.sleep(5)

if __name__ == "__main__":
    print("[INFO] Starting Telegram user status monitor...")
    client.loop.run_until_complete(monitor_users_status())