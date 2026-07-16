import re
from app.config import KEYWORDS

def is_valid_report(text):
    return any(k in text.upper() for k in KEYWORDS)

def parse_message(body):
    pattern = r"(RADAR|AWOS)\s+(\d+)\s+(ON|OFF)"
    match = re.search(pattern, body.upper())
    if match:
        return {
            "type": match.group(1),
            "station": match.group(2),
            "status": match.group(3)
        }
    
    return None