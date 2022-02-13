
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
    bot_token = "5016166355:AAEKxdlkF7ofJNW_bHKZRxl1iRHZlaR519A",
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
    Bot.send_message("@ourclg", "Im started.."+"\n"+dt,reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text='CHECK STATUS', callback_data='alive')]]))
@Bot.on_message(filters.command(["restart"]))
async def restart(c, m):
    k=await m.reply_text("🔄 **Restarting...**")
    sleep(1)
    await k.edit("**cloning repo...**")
    os.system("git clone https://github.com/casperTeam/never1.git")
    sleep(1)
    await k.edit("entering dir")
    sleep(2)
    os.system("cd never1 && python3 main.py")
    await k.edit("🔄 **Starting..bash by python3 main.py**")
    sleep(1)
    await k.edit("**Restarted**")
    await Bot.send_message("@ourclg", "Im started.."+"\n"+dt, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text='CHECK STATUS', callback_data='alive')]]))

print("starting..raaa")
Bot.run()
