import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "30"))

DEVS = list(map(int, os.getenv("DEVS", "8107432436").split()))

API_ID = int(os.getenv("API_ID", "25756091"))

API_HASH = os.getenv("API_HASH", "debddbeeea729aec45b69ad8800c9896")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8122193455:AAHde1ts1g8JbKdIWhN6VZIXFq27alZftmU")

OWNER_ID = int(os.getenv("OWNER_ID", "8107432436"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002704121394").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://kingex:hx7vMVs1iM9EmaKy@kingex.x4ighmk.mongodb.net/?retryWrites=true&w=majority")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002704121394"))
