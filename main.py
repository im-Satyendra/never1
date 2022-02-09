
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

toda = date.today()
today = toda.strftime("%b-%d-%Y")
print(today)
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
with Bot:
    Bot.send_message("@ourclg", "Im started.."+"\n"+today+"\n"+current_time, reply_markup=InlineKeyboardMarkup([InlineKeyboardButton(text='CHECK STATUS', callback_data='amialive')]))
@Bot.on_message(filters.command(["restart"]))
async def restart(c, m):
    k=await m.reply_text("🔄 **Restarting...**")
    sleep(1)
    await k.edit("🔄 **Restarting, Please Wait...**")
    sleep(1)
    await k.edit("**Restarted**")
    await Bot.send_message("@ourclg", "Im started.."+"\n"+today+"\n"+current_time, reply_markup=InlineKeyboardMarkup([InlineKeyboardButton(text='CHECK STATUS', callback_data='amialive')]))

print("starting..raaa")
Bot.run()
