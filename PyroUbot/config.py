import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "30"))

DEVS = list(map(int, os.getenv("DEVS", "6002237323").split()))

API_ID = int(os.getenv("API_ID", "25756091"))

API_HASH = os.getenv("API_HASH", "debddbeeea729aec45b69ad8800c9896")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7771303916:AAGV46bRwqdh_BFs4hRQGISwfH0jAhFgzBc")

OWNER_ID = int(os.getenv("OWNER_ID", "6002237323"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002697921551").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Jefri:Jefri91@cluster0.jdjpg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002697921551"))
