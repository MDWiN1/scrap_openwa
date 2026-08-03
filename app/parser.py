import re
from app.config import KEYWORDS

def is_valid_report(text):
    return any(k in text.upper() for k in KEYWORDS)


def parse_message(body: str):
    body = body.replace("\xa0", " ")

    # Ambil nama site
    site_match = re.search(
        r"status\s+operasional\s+(.*?)(?=\b(?:hari|tanggal|jam|pukul|status|kondisi)\b|$)",
        body,
        re.IGNORECASE | re.DOTALL
    )

    if site_match:
        site_name = site_match.group(1)
        site_name = re.sub(r"\*+", "", site_name).strip()
    else:
        site_name = None

    # Ambil status ON/OFF
    status_match = re.search(
        r"\b(?:status|kondisi)\b\s*[:\-]?\s*\*?\s*(ON|OFF)\b",
        body,
        re.IGNORECASE
    )

    status = status_match.group(1).upper() if status_match else None

    return {
        "site_name": site_name,
        "status": status,
    }