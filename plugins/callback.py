from os import link
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


@Bot.on_callback_query()
async def cdata(c, q):
    data = q.data
    wait = "wait bro..."
    if data.startswith("ss|"):
        link = data.split("|", 1)[1]
        links = (data, link)
        await q.message.edit_text(link)
        await q.answer(links, show_alert=True)
    elif data == "alive":
        ch = q.from_user.mention
        await q.message.edit_text("i am alive\n"+ch, )
        try:
            await Bot.send_message("@ourclg", ch+"\n"+" Iam alive!")
        except Exception as e:
            await Client.send_message("@ourclg", ch+"\n"+" Iam alive!")