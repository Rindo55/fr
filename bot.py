import asyncio
import os
import re
import time
import aiohttp
import requests
import aiofiles
from base64 import standard_b64encode, standard_b64decode
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


from config import Config

logging.getLogger("pyrogram").setLevel(logging.WARNING)
app = Client(
            "Bot",
            bot_token = Config.BOT_TOKEN,
            api_id = Config.API_ID,
            api_hash = Config.API_HASH)

def b64_to_str(b64: str) -> str:
    bytes_b64 = b64.encode('ascii')
    bytes_str = standard_b64decode(bytes_b64)
    __str = bytes_str.decode('ascii')
    return __str
def str_to_b64(__str: str) -> str:

    str_bytes = __str.encode('ascii')

    bytes_b64 = standard_b64encode(str_bytes)

    b64 = bytes_b64.decode('ascii')

    return b64

@app.on_message(filters.command("start") & filters.private)
async def start(bot, cmd: Message):
    usr_cmd = cmd.text.split("_", 1)[-1]
    kay_id = -1001642923224
    if usr_cmd == "/start":
       await cmd.reply_text("Bot seems online! ⚡️")
    else:
        try:
            try:
                file_id = int(b64_to_str(usr_cmd).split("_")[-1])
            except (Error, UnicodeDecodeError):
                file_id = int(usr_cmd.split("_")[-1])
            GetMessage = await app.get_messages(kay_id, message_ids=file_id)
            message_ids = GetMessage.message_id
            await app.copy_message(chat_id=cmd.from_user.id, from_chat_id=kay_id, message_id=message_ids)
        except Exception as err:
            await cmd.reply_text(f"Something went wrong!\n\n**Error:** `XXXXXXX`")
@app.on_message(filters.command("send"))
async def stdart(bot, message: Message):
  sourcetext =  f"**#Encoded_File**" + "\n" + f"**‣ File Name**: ` Ikenaikyo - 01 [720p x265] @animxt.mkv`" + "\n" + "**‣ Video**: `720p HEVC x265 10Bit`" + "\n" + "**‣ Audio**: `Japanese`" + "\n" + "**‣ Subtitle**: `English, Portuguese (Brazil), Spanish (Latin America), Spanish, French, German, Italian, Russian`" + "\n" + "**‣ File Size**: `92 MBs` + "\n" + **‣ Duration:** `24 minutes 42 seconds`" + "\n" + " ** ‣ Downloads:** [🔗Telegram File](https://telegram.me/somayukibot?start=animxt_MjQ1Nw==) 🔗[BETA DL](https://da.gd/ll0oCI)"       
  untextx = await app.send_message(
                      chat_id=-1001159872623,
                      text=sourcetext,
                      reply_to_message_id=35196
)            
            
@app.on_message(filters.command("link") & filters.private)

async def link(bot, cmd: Message):
    usr_cmd = cmd.text.split("_", 1)[-1]
    if usr_cmd == "/link":

       await cmd.reply_text("Fuck off!")

    else: 
        try:

       
            fuk_cmd = cmd.text.replace("/link https://t.me/c/1642923224/", "")
            filex_id = str_to_b64(fuk_cmd)
            sendx = await app.send_message(chat_id=cmd.from_user.id, text="https://t.me/somayukibot?start=animxt_" + filex_id)
        except Exception as err:
            await cmd.reply_text(f"Something went wrong!\n\n**Error:** `XXXXXXX`")

    
app.start()
print("Powered by @animxt")
idle()
