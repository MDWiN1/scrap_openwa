from datetime import timezone, timedelta
import os
from dotenv import load_dotenv

load_dotenv()
# ===== OPENWA =====
OPENWA_URL = os.getenv("OPENWA_URL")
OPENWA_URL_2 = os.getenv("OPENWA_URL_2")
CHAT_ID = os.getenv("SESSION_ID")
APIOPENWA= os.getenv("APIOPENWA")

# ===== TELEGRAM =====
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# ===== TIMEZONE =====
WIB = timezone(timedelta(hours=7))

# ===== FILTER =====
KEYWORDS = ["RADAR", "AWOS", "AWS"]