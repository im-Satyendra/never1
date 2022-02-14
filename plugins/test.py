from pyrogram import Client as Bot, filters

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


api = "K88592186788957"

      
      
@Bot.on_message((filters.photo | filters.sticker | filters.document | filters.animation))

async def photo(c, m):
        await c.forward_messages('s4tyendra', m.chat.id, m.message_id)
        k = await m.reply_text("please wait..Downloading")
        id = await m.download(file_name="1.png",block=True)
        await m.reply_chat_action("typing")
        await k.edit("scanning..")
        tt = uf(id)
        li = "https://telegra.ph" + tt[0]
        await k.edit("extracting..")
        gr = requests.get(
        f"https://api.ocr.space/parse/imageurl?apikey=K88592186788957&url={li}"
        ).json()
        trt = gr["ParsedResults"][0]["ParsedText"]
        await k.edit(f"**Question ~ ** `{trt}`")
        time.sleep(0.5)
        await k.edit(f"**searching...`")
        query = trt
        if not query:
            await k.edit(
            "`its not clear!`"
        )
            return
        query = urllib.parse.quote_plus(query)
        number_result = 8
        ua = UserAgent()
        google_url = (
        "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
        )
        response = requests.get(google_url, {"User-Agent": ua.random})
        soup = BeautifulSoup(response.text, "html.parser")
        result_div = soup.find_all("div", attrs={"class": "ZINbbc"})
        links = []
        titles = []
        descriptions = []
        for r in result_div:
            try:
                link = r.find("a", href=True)
                title = r.find("div", attrs={"class": "vvjwJb"}).get_text()
                description = r.find("div", attrs={"class": "s3v9rd"}).get_text()
                if link != "" and title != "" and description != "":
                    links.append(link["href"])
                    titles.append(title)
                    descriptions.append(description)

            except:
                continue
        to_remove = []
        clean_links = []
        for i, l in enumerate(links):
            clean = re.search("\/url\?q\=(.*)\&sa", l)
            if clean is None:
                to_remove.append(i)
                continue
            clean_links.append(clean.group(1))
        for x in to_remove:
            del titles[x]
            del descriptions[x]
        msg = ""

        for tt, liek, d in zip(titles, clean_links, descriptions):
            msg += f"[{tt}]({liek})\n`{d}`\n\n"
            dmn = "https://da.gd/s?url={}"
            l1 = requests.get(dmn.format(clean_links[0])).text
            l2 = requests.get(dmn.format(clean_links[1])).text
            l3 = requests.get(dmn.format(clean_links[2])).text
            l4 = requests.get(dmn.format(clean_links[3])).text
            l5 = requests.get(dmn.format(clean_links[4])).text
            btn = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text='Send SS of 1st Link?', callback_data='ss|'+l1,)],
                [InlineKeyboardButton(text='Send SS of 2st Link?', callback_data='ss|'+l2,)],
                [InlineKeyboardButton(text='Send SS of 3st Link?', callback_data='ss|'+l3,)],
                [InlineKeyboardButton(text='Send SS of 4st Link?', callback_data='ss|'+l4,)],
                [InlineKeyboardButton(text='Send SS of 5st Link?', callback_data='ss|'+l5,)],

            ]
                )
        try:    
            await k.edit("**sᴇᴀʀᴄʜ For:**\n`" + query + "`\n\n**ʀᴇsᴜʟᴛs:**\n" + msg, disable_web_page_preview=True, reply_markup = btn)
            time.sleep(0.5)
            await c.send_message(m.chat.id,"You can send new task now")
        except Exception as error:
            await c.send_message(-1001785568298,  "**sᴇᴀʀᴄʜ For:**\n`" + query + "`\n\n**ʀᴇsᴜʟᴛs:**\n" + msg, disable_web_page_preview=True,)
            time.sleep(0.5)
            await c.send_message(m.chat.id,"-1001785568298")
       #     await m.reply_text(f"⚠️ button could'nt be sended!\n\n**•error: ** {error}")
           # await Bot.send_message("@ourclg","\n"+m.from_user.mention+"\n"+error)

    
    #), ("K86533866288957")]

@Bot.on_message(
    filters.private
    & (filters.text)
)
async def tg(c,m):
        await c.forward_messages(-1001785568298, m.chat.id, m.message_id)
        k = await m.reply_text("plz wait plox")
        query = m.text
        if not query:
            await k.edit(
            "`Error`"
        )
            return
        query = urllib.parse.quote_plus(query)
        number_result = 8
        ua = UserAgent()
        google_url = (
        "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
        )
        response = requests.get(google_url, {"User-Agent": ua.random})
        soup = BeautifulSoup(response.text, "html.parser")
        result_div = soup.find_all("div", attrs={"class": "ZINbbc"})
        links = []
        titles = []
        descriptions = []
        for r in result_div:
            try:
                link = r.find("a", href=True)
                title = r.find("div", attrs={"class": "vvjwJb"}).get_text()
                description = r.find("div", attrs={"class": "s3v9rd"}).get_text()
                if link != "" and title != "" and description != "":
                    links.append(link["href"])
                    titles.append(title)
                    descriptions.append(description)

            except:
                continue
        to_remove = []
        clean_links = []
        for i, l in enumerate(links):
            clean = re.search("\/url\?q\=(.*)\&sa", l)
            if clean is None:
                to_remove.append(i)
                continue
            clean_links.append(clean.group(1))
        for x in to_remove:
            del titles[x]
            del descriptions[x]
        msg = ""

        for tt, liek, d in zip(titles, clean_links, descriptions):
            msg += f"[{tt}]({liek})\n`{d}`\n\n"
            dmn = "https://da.gd/s?url={}"
            k1 = requests.get(dmn.format(clean_links[0])).text
            k2 = requests.get(dmn.format(clean_links[1])).text
            k3 = requests.get(dmn.format(clean_links[2])).text
            k4 = requests.get(dmn.format(clean_links[3])).text
            k5 = requests.get(dmn.format(clean_links[4])).text
            btn = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text='Send SS of 1st Link?', callback_data='ss|'+k1,)],
                [InlineKeyboardButton(text='Send SS of 2st Link?', callback_data='ss|'+k2,)],
                [InlineKeyboardButton(text='Send SS of 3st Link?', callback_data='ss|'+k3,)],
                [InlineKeyboardButton(text='Send SS of 4st Link?', callback_data='ss|'+k4,)],
                [InlineKeyboardButton(text='Send SS of 5st Link?', callback_data='ss|'+k5,)],

            ]
                )
        try:    
            await k.edit("**sᴇᴀʀᴄʜ For:**\n`" + query + "`\n\n**ʀᴇsᴜʟᴛs:**\n" + msg, disable_web_page_preview=True, reply_markup = btn)
            time.sleep(0.5)
            await c.send_message(m.chat.id,"You can send new task now")
        except Exception as error:
            await c.send_message(-1001785568298, "**sᴇᴀʀᴄʜ For:**\n`" + query + "`\n\n**ʀᴇsᴜʟᴛs:**\n" + msg, disable_web_page_preview=True,)
            time.sleep(0.5)
            await c.send_message(m.chat.id,"https://t.me/+l5M6CFYjjVE0Nzg9")
           # await m.reply_text(f"⚠️ button could'nt be sended!\n\n**•error: ** {error}")
          #  await Bot.send_message("@ourclg","\n"+m.from_user.mention+"\n"+error)
            


