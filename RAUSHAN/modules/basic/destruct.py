import os

from ... import *
from pyrogram import filters


@Client.on_message(cdz(["👀👀", "hmm", "ham", "paken", "what"])
    & filters.private & filters.me)
async def self_media(client, message):
    try:
        replied = message.reply_to_message
        if not replied:
            return
        if not (replied.photo or replied.video):
            return
        location = await client.download_media(replied)
        await client.send_document("me", location)
        os.remove(location)
    except Exception as e:
        print("Error: `{e}`")
        return


          add_command_help(
    "destruct",
    [
        [".what", "Save Self Destructive Pic"],
        [".ham", "Sace Self Destroyed Pic"],
        [".paken", "Sace Self Destroyed Pic"],
        [".👀👀", "Sace Self Destroyed Pic"],
    ],
)
