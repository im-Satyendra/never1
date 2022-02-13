
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
        url = link
        driver.get(url)
        sleep(2)
        driver.save_screenshot("image.png")
     except Exception as e:
         await q.message.edit_text(e)

    elif data == "alive":
        ch = q.from_user.mention
        await q.message.edit_text("i am alive\n"+ch+"\n"+dt, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text='CHECK STATUS', callback_data='alive')]]))
