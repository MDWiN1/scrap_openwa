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
    #print(res.text)


# def send_long_message1(text):
#     max_len = 4000
#     for i in range(0, len(text), max_len):
#         send_message(text[i:i+max_len])


def send_long_message(text_input):
    max_len = 4000

    # Check if the input is a list/tuple of multiple report blocks
    if isinstance(text_input, (list, tuple)):
        for single_block in text_input:
            # Recursively call this function for each block to ensure length protection
            send_long_message(single_block)
        return  # Exit early after processing the list

    # If it is a single string text block, execute standard chunking logic
    for i in range(0, len(text_input), max_len):
        send_message(text_input[i: i + max_len])