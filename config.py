import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "8045459")) #optional
API_HASH = getenv("API_HASH", "e6d1f09120e17a4372fe022dde88511b") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8187361583 1281282633").split()))
OWNER_ID = int(getenv("OWNER_ID", "1281282633"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://heartbeat:Beat7Heart@heartbeat.1h1nbxv.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "7068876137:AAHxyBy6P_UBAL-5eS9S6YBIGAlSyWJ03HA")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://graph.org/file/9ee37cccd7bf55c3ec953.png')
ALIVE_TEXT = getenv("ALIVE_TEXT", "ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙᴇ..🏓 \n\n\n ᴘᴏᴡᴇʀᴇᴅ ʙʏ ❤️ \n[𝅗ـﮩ٨ـ𝅽𝅾𓆩𝐇𖽞𖽖‌֯֟፝‌𖽸𖾓𝂬𓏲ࣹ᷼𝄢𝂬𝐁𖽞‌֟֠֯፝‌𖽖𖾓𓆪ﮩ٨ـ𝅽𝅾‐𝅘▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ](https://t.me/HeartBeat_Muzic)")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP", "-1001735663878")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://t.me/HeartBeat_Muzic")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQB6w5MAPCnQr_8FstvmjZyBBPo4EW7vQLdNQU2vgiWbL8t-vE74iiDVLEVMnIbtctM7sfp4QDa4vpV03WqvbehCyJeoxOtmv58KcDG214dQZ81iAWclihGUHB3b-mjSsTVwarUOzM70DMDyGWPlu2odFxYELBQUVr_Go9hRcLeaYg-0Q8ldL6KiIxpQMHjlnwHefLxPvm1Z_jXNfuI0zuOK6R81YSTqaqIOOavO4e6ntZsYxDc39k4cOxZCUP1-Ijo6x_tSYptSq-RWXhvUfJ6wCR_XI7HDz3dcAZQ8IxeWiguW5VgG572JZyjy30z62pCgUl48EAWNC9l8UL7HSG5pUT3RCwAAAABMXtJJAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
