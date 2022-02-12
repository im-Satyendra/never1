
from pyrogram import Client, filters
from time import sleep
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging
from tglogging import TelegramLogHandler

# TelegramLogHandler is a custom handler which is inherited from an existing handler. ie, StreamHandler.

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        TelegramLogHandler(
            token="5016166355:AAEKxdlkF7ofJNW_bHKZRxl1iRHZlaR519A", 
            log_chat_id=-1001543238877, 
            update_interval=2, 
            minimum_lines=1, 
            pending_logs=200000),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

logger.info("live log streaming to telegram.")

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
    await k.edit("🔄 **Restarting, Please Wait...**")
    sleep(1)
    await k.edit("**Restarted**")
    await Bot.send_message("@ourclg", "Im started.."+"\n"+dt, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text='CHECK STATUS', callback_data='alive')]]))

print("starting..raaa")
Bot.run()
