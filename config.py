import os
from dotenv import load_dotenv
import logging

logging.basicConfig(
    format="%(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

load_dotenv()


class Config(object):
    # Bot token from BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7277194738:AAHrewQsvKcPqeXYeMIbSk-nyUjgJ14kW8U")
    
    # Telegram API details
    API_ID = int(os.environ.get("API_ID", "22141398"))
    API_HASH = os.environ.get("API_HASH", "0c8f8bd171e05e42d6f6e5a6f4305389")

    # File / Video download location
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size (around 4GB)
    TG_MAX_FILE_SIZE = 4194304000

    # Chunk size for downloads/uploads
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    # Proxy if needed
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    # Subprocess timeout
    PROCESS_MAX_TIMEOUT = 3700

    # Owner ID
    OWNER_ID = 5660839376

    # Admins who can access full bot
    AUTH_USERS = [5660839376, 6167872503, 5961011848]

    # Log and Dump Channels
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002284232975"))
    DUMP_CHANNEL = int(os.environ.get("DUMP_CHANNEL", "-1002284232975"))

    # Force Sub Channel
    FORCE_CHANNEL = int(os.environ.get("FORCE_CHANNEL", "-1002379643238"))

    # MongoDB Config
    MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://Ansh089:Ansh089@cluster0.y8tpouc.mongodb.net/?retryWrites=true&w=majority")
    MONGO_NAME = os.environ.get("MONGO_NAME", "URLUPLOADER-DL")

    # Session Name
    SESSION = os.environ.get("SESSION", "teraboxdl")

    # Port for Webhook or server
    PORT = int(os.environ.get("PORT", "8080"))

    # Daily User Limits
    DAILY_LIMITS = int(os.environ.get("DAILY_LIMITS", "20"))

    # Maintenance Mode
    MAINTENANCE_MODE = bool(os.environ.get("MAINTENANCE_MODE", False))

    # Maintenance Message
    MAINTENANCE_MESSAGE = (
        "⚠️ **Maintenance Mode Activated** ⚙️\n\n"
        "Our bot is currently undergoing scheduled maintenance to improve performance and add new features.\n\n"
        "Please check back in a while. We’ll be back soon, better than ever!\n\n"
        "💬 **Support Group:** [SUPPORT](https://t.me/AnSBotsSupports)\n\n"
        "**– Team Support**"
    )
