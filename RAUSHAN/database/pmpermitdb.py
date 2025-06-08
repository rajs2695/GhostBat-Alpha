from RAUSHAN.database import cli
import asyncio

collection = cli["RAUSHAN"]["pmpermit"]

PMPERMIT_MESSAGE = (
   "**☆ . * ● ¸ . ✦ .★　° :. ★ * • ○ ° ★\n\nʜᴇʏ ɪ'ᴍ 𝐇𝐞𝐚𝐫𝐭𝐁𝐞𝐚𝐭-✗-𝐁𝐨𝐭\n\n☆ . * ● ¸ . ✦ .★　° :. ★ * • ○ ° ★\n\n➽─────────────────❥\n\n💕 ᴛᴀɢ ᴍʏ ʟᴏᴠᴇ 🦋\n https://t.me/HeartBeat_Muzic \n\n➽─────────────────❥\n\n😈 ᴏᴛʜᴇʀᴡɪꜱᴇ, ᴡᴀɪᴛ ᴜɴᴛɪʟ ᴍʏ ʙᴏꜱꜱ ᴄᴏᴍᴇꜱ, ᴅᴏɴ'ᴛ ꜱᴘᴀᴍ ᴍᴇ..\nʏᴏᴜ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏʙʟᴏᴄᴋ (ᴜᴘᴛᴏ 3 ᴍᴇꜱꜱᴀɢᴇꜱ)\n\n**☆ . * ● ¸ . ✦ .★　° :. ★ * • ○ ° ★**"
)

BLOCKED = "**ʙᴇᴇᴘ ʙᴏᴏᴘ ꜰᴏᴜɴᴅᴇᴅ ᴀ ꜱᴘᴀᴍᴍᴇʀ!, ʙʟᴏᴄᴋᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!\n\n ʀᴇ𝗊ᴜᴇ𝗌ᴛ ᴛᴏ 𝗎𝗇𝖻𝗅𝗈𝖼𝗄 \n [𝅗ـﮩ٨ـ𝅽𝅾𓆩𝐇𖽞𖽖֯֟፝͢͡𖽸𖾓𝂬𓏲ࣹ᷼𝄢𝂬𝐁𖽞֟֠֯፝͢͡𖽖𖾓𓆪ﮩ٨ـ𝅽𝅾‐𝅘▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ](https://t.me/HeartBeat_Muzic)**"

LIMIT = 3

ALIVE_PIC = "https://graph.org/file/9ee37cccd7bf55c3ec953.png"


async def set_pm(value: bool):
    doc = {"_id": 1, "pmpermit": value}
    doc2 = {"_id": "Approved", "users": []}
    r = await collection.find_one({"_id": 1})
    r2 = await collection.find_one({"_id": "Approved"})
    if r:
        await collection.update_one({"_id": 1}, {"$set": {"pmpermit": value}})
    else:
        await collection.insert_one(doc)
    if not r2:
        await collection.insert_one(doc2)


async def set_permit_message(text):
    await collection.update_one({"_id": 1}, {"$set": {"pmpermit_message": text}})


async def set_block_message(text):
    await collection.update_one({"_id": 1}, {"$set": {"block_message": text}})


async def set_limit(limit):
    await collection.update_one({"_id": 1}, {"$set": {"limit": limit}})


async def get_pm_settings():
    result = await collection.find_one({"_id": 1})
    if not result:
        return False
    pmpermit = result["pmpermit"]
    pm_message = result.get("pmpermit_message", PMPERMIT_MESSAGE)
    block_message = result.get("block_message", BLOCKED)
    limit = result.get("limit", LIMIT)
    return pmpermit, pm_message, limit, block_message


async def allow_user(chat):
    doc = {"_id": "Approved", "users": [chat]}
    r = await collection.find_one({"_id": "Approved"})
    if r:
        await collection.update_one({"_id": "Approved"}, {"$push": {"users": chat}})
    else:
        await collection.insert_one(doc)


async def get_approved_users():
    results = await collection.find_one({"_id": "Approved"})
    if results:
        return results["users"]
    else:
        return []


async def deny_user(chat):
    await collection.update_one({"_id": "Approved"}, {"$pull": {"users": chat}})


async def pm_guard():
    result = await collection.find_one({"_id": 1})
    if not result:
        return False
    if not result["pmpermit"]:
        return False
    else:
        return True
