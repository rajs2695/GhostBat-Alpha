import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "8045459")) #optional
API_HASH = getenv("API_HASH", "e6d1f09120e17a4372fe022dde88511b") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8187361583 1281282633").split()))
OWNER_ID = int(getenv("OWNER_ID", "1281282633"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://ftyvfbgubhu7:hDZwwlNzlKBzls84@ameliamusicbot.f7dzw.mongodb.net/?retryWrites=true&w=majority&appName=AmeliaMusicbot")
BOT_TOKEN = getenv("BOT_TOKEN", "2132260441:AAGPjMCj6vq5_xhcZoxluYFJ_egPrSm1o6U")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://graph.org/file/9ee37cccd7bf55c3ec953.png')
ALIVE_TEXT = getenv("ALIVE_TEXT", "ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙᴇ..🏓 \n\n\n ᴘᴏᴡᴇʀᴇᴅ ʙʏ ❤️ \n𝅗ـﮩ٨ـ𝅽𝅾𓆩𝐇𖽞𖽖‌֯֟፝‌𖽸𖾓𝂬𓏲ࣹ᷼𝄢𝂬𝐁𖽞‌֟֠֯፝‌𖽖𖾓𓆪ﮩ٨ـ𝅽𝅾‐𝅘▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP", "2588523310")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://t.me/HeartBeat_Muzic")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQHEb5wAjh-VJhJTbGAt_16pIrZF4l6cjP-QxNGnnWSaWCZK7VXM4CeOa-7tvG2zawSFwjJ7j-2RgUSRQFMVNQG1MClEtmKV7gdGGiLliJLyQdAbclUPdpkqSWtyiQHrpekPh98VVCOPR97aryTuNZ1fDfIb5_fq0Ik1HTJNV3pv-YMpL2bcpM6r24rDmu_9v9L1wSkaZAQfXTPFNLZuuOspTwWFf-SWu15jYNn8KGohQOalyPkIDWCozJYarP4gwokvEb4EM55nP7GgeQFmc9YymT0hGoDQfNF91g-AOmCWTSqp2o9rU5EojNImgDc91TbCHS8u7k7TvHixm_JJF2NXzzf6RwAAAAHHZ9BxAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
