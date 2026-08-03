import requests
from app.config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }

    res = requests.post(url, json=payload)
    res.raise_for_status()
    print(res.text)


def send_long_message(text):
    max_len = 4000
    for i in range(0, len(text), max_len):
        send_message(text[i:i+max_len])