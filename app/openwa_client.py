import requests
from app.config import APIOPENWA,OPENWA_URL_2


def get_messages(limit=300):
    params = {
        "limit": limit
    }
    headers = {
        "X-API-Key": APIOPENWA
    }
    res = requests.get(OPENWA_URL_2, headers=headers,params=params, verify=False)
    res.raise_for_status()
    data = res.json()
    return data.get("messages", [])