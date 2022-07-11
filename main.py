
from pyrogram import Client, filters
from time import sleep
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import os

plugins = dict(
    root="plugins"
)

Bot = Client(
    "bot",
    bot_token = "5526290298:AAEobpFpHx8MEp2jkttD_j4z9XCnLTeYAlQ",
    api_id = 2171111,
    api_hash = "fd7acd07303760c52dcc0ed8b2f73086",
    plugins=plugins,
)
import pytz
from datetime import date, datetime
UTC = pytz.utc
IST = pytz.timezone('Asia/Kolkata')
datetime_ist = datetime.now(IST)
dt = datetime_ist.strftime('%Y:%m:%d %H:%M:%S')
print(dt)
with Bot:
    Bot.send_message(-1001497428213, "Im started.."+"\n"+dt,reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text='CHECK STATUS', callback_data='alive')]]))
@Bot.on_message(filters.command(["restart"]))
async def restart(_, message):
    m = message
    id = m.from_user.id
    if id != 1089528685:
        await m.delete()
        time.sleep(3)
        mm = await m.reply_sticker(
            "CAACAgUAAx0CYF-hHQACVotid_YH5QunOUMFwF2C1HwkWEjGNAAC6wIAAsYNkFeYvtc3bIYTMB4E"
        )
        await m.reply_text(
            "contact @s4tyendra to use this bot\nor wait a week! and dont block me"
        )

print("starting..raaa")
Bot.run()
