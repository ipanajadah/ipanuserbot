import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "30"))

DEVS = list(map(int, os.getenv("DEVS", "7845730448").split()))

API_ID = int(os.getenv("API_ID", "27436953"))

API_HASH = os.getenv("API_HASH", "f83021143420765793bebf4f50cbd969")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8106486428:AAFbOQLe4J6BywKnYn0MlwnB3fUyt4Ug_gs")

OWNER_ID = int(os.getenv("OWNER_ID", "7845730448"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002328852888").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Ipanndongok:Ipanndongok@ipanndongok.bg7xf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002566228411"))
