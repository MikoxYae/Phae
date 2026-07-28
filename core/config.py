from __future__ import annotations
import logging
from pathlib import Path

import config as user_config

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
DOWNLOAD_DIR = BASE_DIR / "anime_downloads"
THUMBNAIL_DIR = BASE_DIR / "thumbnails"

for directory in [LOG_DIR, DOWNLOAD_DIR, THUMBNAIL_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "bot.log"
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler(), logging.FileHandler(str(LOG_FILE))],
)
logger = logging.getLogger(__name__)

API_ID = int(user_config.API_ID)
API_HASH = str(user_config.API_HASH).strip()
BOT_TOKEN = str(user_config.BOT_TOKEN).strip()
ADMINS = [int(admin_id) for admin_id in user_config.ADMINS]
OWNER_ID = int(getattr(user_config, "OWNER_ID", ADMINS[0]))
ADMIN_CHAT_ID = OWNER_ID
BOT_USERNAME = str(getattr(user_config, "BOT_USERNAME", "")).strip().lstrip("@")

MONGO_URI = getattr(user_config, "MONGO_URI", None)
DB_NAME = str(getattr(user_config, "DB_NAME", "AnimePahe"))
PORT = int(getattr(user_config, "PORT", 3409))
WEB_PORT = PORT

CHANNEL_ID = getattr(user_config, "CHANNEL_ID", None)
CHANNEL_NAME = str(getattr(user_config, "CHANNEL_NAME", ""))
CHANNEL_USERNAME = str(getattr(user_config, "CHANNEL_USERNAME", "")).strip()
DUMP_CHANNEL_ID = getattr(user_config, "DUMP_CHANNEL_ID", None)
DUMP_CHANNEL_USERNAME = str(getattr(user_config, "DUMP_CHANNEL_USERNAME", "")).strip()

if CHANNEL_ID not in (None, ""):
    CHANNEL_ID = int(CHANNEL_ID)
else:
    CHANNEL_ID = None
if DUMP_CHANNEL_ID not in (None, ""):
    DUMP_CHANNEL_ID = int(DUMP_CHANNEL_ID)
else:
    DUMP_CHANNEL_ID = None
if CHANNEL_USERNAME:
    CHANNEL_USERNAME = CHANNEL_USERNAME.lstrip("@")
if DUMP_CHANNEL_USERNAME:
    DUMP_CHANNEL_USERNAME = "@" + DUMP_CHANNEL_USERNAME.lstrip("@")

FIXED_THUMBNAIL_URL = str(getattr(user_config, "FIXED_THUMBNAIL_PIC", ""))
START_PIC_URL = str(getattr(user_config, "START_PIC_URL", ""))
DELETE_TIMER = int(getattr(user_config, "DELETE_TIMER", 1800))
FFMPEG_PATH = str(getattr(user_config, "FFMPEG_PATH", "ffmpeg"))

AUTO_DOWNLOAD_STATE_FILE = BASE_DIR / "auto_download_state.json"
QUALITY_SETTINGS_FILE = BASE_DIR / "quality_settings.json"
SESSION_FILE = BASE_DIR / "anime_bot.session"
JSON_DATA_FILE = BASE_DIR / "anime_data.json"

required = {
    "API_ID": API_ID,
    "API_HASH": API_HASH,
    "BOT_TOKEN": BOT_TOKEN,
    "ADMINS": ADMINS,
}
missing = [name for name, value in required.items() if not value]
if missing:
    raise ValueError(f"Missing required values in config.py: {', '.join(missing)}")

class Config:
    API_ID = API_ID
    API_HASH = API_HASH
    BOT_TOKEN = BOT_TOKEN
    ADMINS = ADMINS
    OWNER_ID = OWNER_ID
    MONGO_URI = MONGO_URI
    DB_NAME = DB_NAME
    PORT = PORT

logger.info("Configuration loaded from root config.py")

HEADERS = {
    'authority': 'animepahe.pw',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__ddg2_=;',
    'dnt': '1',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="124", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://animepahe.pw/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

ANILIST_API = "https://graphql.anilist.co"

ANILIST_API = "https://graphql.anilist.co"

SEARCH, SELECT_ANIME, SELECT_EPISODE, SELECT_QUALITY, DOWNLOADING = range(5)
AUTO_DISABLED, AUTO_ENABLED = range(2)

WEB_PORT = PORT

HELP_TEXT='''<b>
<blockquote>✦ 𝗛𝗘𝗟𝗣𝗘𝗥 ✦</blockquote>
──────────────────
<blockquote>シ 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦:</blockquote>
<blockquote expandable><code>/cancel</code> - ᴄᴀɴᴄᴇʟ ᴄᴜʀʀᴇɴᴛ ᴏᴘᴇʀᴀᴛɪᴏɴ
<code>/latest</code> - ɢᴇᴛ ʟᴀᴛᴇsᴛ ᴀɪʀɪɴɢ ᴀɴɪᴍᴇ
<code>/airing</code> - ɢᴇᴛ ᴄᴜʀʀᴇɴᴛʟʏ ᴀɪʀɪɴɢ ᴀɴɪᴍᴇ
<code>/del_timer</code> - sᴇᴛ ғɪʟᴇ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇʀ
<code>/addchnl [id] [name]</code> - sᴇᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ
<code>/removechnl [id] [name]</code> - ʀᴇᴍᴏᴠᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ
<code>/listchnl</code> - sʜᴏᴡ ᴀʟʟ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟs ᴀs ᴀ ʟɪsᴛ
<code>/set_request_time [HH:MM]</code> - sᴇᴛ ᴅᴀɪʟʏ ʀᴇǫᴜᴇsᴛ ᴘʀᴏᴄᴇssɪɴɢ ᴛɪᴍᴇ (IST)
<code>/set_max_requests [number]</code> - sᴇᴛ ᴍᴀxɪᴍᴜᴍ ɴᴜᴍʙᴇʀ ᴏғ ᴄᴏɴᴄᴜʀʀᴇɴᴛ ʀᴇǫᴜᴇsᴛs
<code>/view_requests</code> - sʜᴏᴡ ᴘᴇɴᴅɪɴɢ ʀᴇǫᴜᴇsᴛs
<code>/set_request_group [group_id]</code> - sᴇᴛ ᴛʜᴇ ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ
<code>/request [anime name]</code> or <code>
<code>/addtask [number]</code> - ᴅᴏᴡɴʟᴏᴀᴅ sᴘᴇᴄɪғɪᴄ ᴀɴɪᴍᴇ ғʀᴏᴍ ʟᴀᴛᴇsᴛ ᴀɪʀɪɴɢ ʟɪsᴛ
<code>/redownload [number]</code> - ғᴏʀᴄᴇ ʀᴇᴅᴏᴡɴʟᴏᴀᴅ ᴀ sᴘᴇᴄɪғɪᴄ ᴀɴɪᴍᴇ
<code>/add_admin [user_id]</code> - ᴀᴅᴅ ᴀ ɴᴇᴡ ᴀᴅᴍɪɴ
<code>/remove_admin [user_id]</code> - ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ</blockquote expandable>
──────────────────
<blockquote>≡ ᴘᴏᴡᴇʀᴇᴅ ʙʏ: <a href='t.me/GenAnimeOngoing'>𝗢𝗻𝗴𝗼𝗶𝗻𝗴 𝗔𝗻𝗶𝗺𝗲 - 𝗪𝗶𝗻𝘁𝗲𝗿 𝟮𝟬𝟮𝟲</a></blockquote></b>'''

