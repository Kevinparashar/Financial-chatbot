import json
import os
from langdetect import detect

HISTORY_FILE = "history/chat_logs.json"

def log_history(query, response):
    os.makedirs("history", exist_ok=True)
    entry = {"query": query, "response": response}
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    else:
        history = []
    history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"