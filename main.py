
from pyrogram import Client, filters
from time import sleep
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
plugins = dict(
    root="plugins"
)

Bot = Client(
    "bot",
    bot_token = "5016166355:AAEKxdlkF7ofJNW_bHKZRxl1iRHZlaR519A",
    api_id = 2171111,
    api_hash = "fd7acd07303760c52dcc0ed8b2f73086",
    plugins=plugins,
)
from datetime import date, datetime

import pytz

UTC = pytz.utc
  

IST = pytz.timezone('Asia/Kolkata')

print("IST in Default Format : ",datetime.now(IST))
datetime_ist = datetime.now(IST)
dt = datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z')
with Bot:
    Bot.send_message("@ourclg", "Im started.."+"\n"+dt, reply_markup=InlineKeyboardMarkup([InlineKeyboardButton(text='CHECK STATUS', callback_data='amialive')]))
@Bot.on_message(filters.command(["restart"]))
async def restart(c, m):
    k=await m.reply_text("🔄 **Restarting...**")
    sleep(1)
    await k.edit("🔄 **Restarting, Please Wait...**")
    sleep(1)
    await k.edit("**Restarted**")
    await Bot.send_message("@ourclg", "Im started.."+"\n"+dt, reply_markup=InlineKeyboardMarkup([InlineKeyboardButton(text='CHECK STATUS', callback_data='amialive')]))

print("starting..raaa")
Bot.run()
