
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "8145348652").split()))

API_ID = int(os.getenv("API_ID", "13599761"))

API_HASH = os.getenv("API_HASH", "76a1d92c30ab71327239fde935f3060a")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7915079265:AAF_n0PIhJ49NIueKObPWWZ9mJtzpe8SbDA")

OWNER_ID = int(os.getenv("OWNER_ID", "8145348652"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002419662880").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Ipanndongok:Ipanndongok@ipanndongok.bg7xf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", " -1002419662880"))
