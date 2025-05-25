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
BOT_TOKEN = getenv("BOT_TOKEN", "7068876137:AAG915L7WDo-X7t3kY38PDkIZ5-XEp-AjF8")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://graph.org/file/9ee37cccd7bf55c3ec953.png')
ALIVE_TEXT = getenv("ALIVE_TEXT", "ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙᴇ..🏓 \n\n\n ᴘᴏᴡᴇʀᴇᴅ ʙʏ ❤️ \n𝅗ـﮩ٨ـ𝅽𝅾𓆩𝐇𖽞𖽖‌֯֟፝‌𖽸𖾓𝂬𓏲ࣹ᷼𝄢𝂬𝐁𖽞‌֟֠֯፝‌𖽖𖾓𓆪ﮩ٨ـ𝅽𝅾‐𝅘▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP", "2588523310")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://t.me/HeartBeat_Muzic")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQFexMIAK6_AlJ-BICzRw9v4KvKJacN5SJIWK2oT8qawL5XSM_x1IMTNG1yfsTiOkWzERUPQm13qJNvxyYCXCRAiCbtMbTX8HD-qCkQulkPmKkI3yL2nN6MvvmmyxY0EtSMeutPfmSgcVCt5PzgUBsp4J9lx4-H7diK2VLrIw66X5ryYv6WNpD1NQFv_pyaE-ASeUwVK9ZlQfpOsPBUE-7kdmTRVBiNM2OPcfSCWsixDUy7Pz5Y3ZZOXlTECsdEpCAbljVxL9ry77zIoKLi7xui_yjKADkZI0ChFIoyqxurnIjpAmsursxOPis0Gs-yio5lqevJjbmX79bYYJVjtc6eYeor2vQAAAAHoATkvAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
