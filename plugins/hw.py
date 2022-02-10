from pyrogram import Client as Bot, filters
@Bot.send_message(filters.command("che"))
async def che(c, m):
  await m.reply_text("YOU ARE NOT  AUTHORISED!")
