
from pyrogram import Client as Bot, filters
from pyrogram import client
import requests
from pyrogram import Client, filters
from pyrogram.types import *
import requests
import re
import urllib
import urllib.parse
import sys
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client as Bot, filters
import re
import time 
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pyrogram import Client, filters
from telegraph import upload_file as uf
import requests
from bs4 import BeautifulSoup
import pytz
from datetime import date, datetime
UTC = pytz.utc
IST = pytz.timezone('Asia/Kolkata')
datetime_ist = datetime.now(IST)
dt = datetime_ist.strftime('%Y:%m:%d %H:%M:%S')
from time import sleep
import argparse
from selenium import webdriver
from PIL import Image
import asyncio
import os
import aiofiles
# url list to screenshot


# defining options manually

# actually launching the function

@Bot.on_callback_query()
async def cdata(c, q):
    data = q.data
    wait = "wait bro..."
    driver = webdriver.Chrome()
    if data.startswith("ss|"):
     try:
            link = data.split("|", 1)[1]
            await q.answer("Processing...", show_alert=True)
            await q.message.edit_text("`Processing ...`")
            chrome_options = webdriver.ChromeOptions()
            chrome_options.binary_location = Config.GOOGLE_CHROME_BIN
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument("--test-type")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument('--disable-gpu')
            driver = webdriver.Chrome(chrome_options=chrome_options)
            driver.get(link)
            height = driver.execute_script(
        "return Math.max(document.body.scrollHeight, document.body.offsetHeight, "
        "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
        "document.documentElement.offsetHeight);")
            width = driver.execute_script(
        "return Math.max(document.body.scrollWidth, document.body.offsetWidth, "
        "document.documentElement.clientWidth, document.documentElement.scrollWidth, "
        "document.documentElement.offsetWidth);")
            driver.set_window_size(width + 125, height + 125)
            wait_for = height / 1000
            await q.message.edit_text(f"`Generating screenshot of the page...`"
                       f"\n`Height of page = {height}px`"
                       f"\n`Width of page = {width}px`"
                       f"\n`Waiting ({int(wait_for)}s) for the page to load.`")
            await asyncio.sleep(int(wait_for))
            im_png = driver.get_screenshot_as_png()
            driver.close()
            file_path = os.path.join("ss", "webss.png")
            async with aiofiles.open(file_path, 'wb') as out_file:
               await out_file.write(im_png)
            await asyncio.gather(
                Bot.send_document(chat_id=q.from_user.id,
                                     document=file_path,
                                     caption=link,)
            )
            os.remove(file_path)
            driver.quit()

     except Exception as e:
         await q.message.edit_text(e)

    elif data == "alive":
        ch = q.from_user.mention
        await q.message.edit_text("i am alive\n"+ch+"\n"+dt, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text='CHECK STATUS', callback_data='alive')]]))
