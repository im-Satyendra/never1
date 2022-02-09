
from pyrogram import Client, filters
from time import sleep

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
with Bot:
    Bot.send_message("@ourclg", "Im started..")
@Bot.on_message(filters.command(["restart"]))
async def restart(c, m):
    k=await m.reply_text("🔄 **Restarting...**")
    sleep(1)
    await k.edit("🔄 **Restarting, Please Wait...**")
    sleep(1)
    await k.edit("**Restarted**")
    await Bot.send_message("@ourclg", "Im started..")

print("starting..raaa")
Bot.run()
