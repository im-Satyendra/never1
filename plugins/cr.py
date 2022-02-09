import os
import re
import io
import sys
import traceback
import subprocess
from inspect import getfullargspec
from pyrogram.types import Message
from pyrogram import Client, filters
import requests ,lxml, json 
from bs4 import BeautifulSoup 
from datetime import datetime, time, timedelta 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


CMD_HNDLR = ["!"]

async def pexec(code, client, message):
    exec(
        f"async def __aexec(client, message): "
        + "".join(f"\n {a}" for a in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)


async def texec(code, smessatatus):
    message = event = smessatatus
    p = lambda _x: print(_format.yaml_format(_x))
    reply = await event.get_reply_message()
    exec(
        f"async def __aexec(message, event , reply, client, p, chat): "
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](
        message, event, reply, message.client, p, message.chat_id
    )


async def edit_or_reply(msg: Message, **kwargs):
    func = msg.edit_text if msg.from_user.is_self else msg.reply
    spec = getfullargspec(func.__wrapped__).args
    await func(**{k: v for k, v in kwargs.items() if k in spec})


# shell runner
@Client.on_message(filters.command(["sh"], CMD_HNDLR))
async def shellrunner(client, message):
    if len(message.command) < 2:
        return await edit_or_reply(
            message, text="__Nigga give me some command to execute!__"
        )
    try:
        text = message.text.split(None, maxsplit=1)[1]
    except IndexError:
        return await message.delete()
    if "\n" in text:
        code = text.split("\n")
        output = ""
        for x in code:
            shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", x)
            try:
                process = subprocess.Popen(
                    shell,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
            except Exception as err:
                print(err)
                await edit_or_reply(message, text=f"► **ERROR:**\n```{err}```")
            output += f"**{code}**\n"
            output += process.stdout.read()[:-1].decode("utf-8")
            output += "\n"
    else:
        shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", text)
        for a in range(len(shell)):
            shell[a] = shell[a].replace('"', "")
        try:
            process = subprocess.Popen(
                shell,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except Exception as err:
            print(err)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errors = traceback.format_exception(
                etype=exc_type,
                value=exc_obj,
                tb=exc_tb,
            )
            return await edit_or_reply(
                message, text=f"► **ERROR:**\n```{''.join(errors)}```"
            )
        output = process.stdout.read()[:-1].decode("utf-8")
    if str(output) == "\n":
        output = None
    if output:
        if len(output) > 4096:
            with open("output.txt", "w+") as file:
                file.write(output)
            await client.send_document(
                message.chat.id,
                "output.txt",
                caption="`Output`",
                reply_to_message_id=message.message_id
            )
            return os.remove("output.txt")
        await edit_or_reply(message, text=f"► **OUTPUT:**\n```{output}```")
    else:
        await edit_or_reply(message, text="► **OUTPUT:**\n`No output`")


# pyrogram executor
@Client.on_message(filters.command(["eval"], CMD_HNDLR))
async def pyroexecutor(client, message):
    if len(message.command) < 2:
        return await message.reply(
            "__Nigga give me some command to execute!__"
        )
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await message.delete()
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await pexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = f"► **OUTPUT:**\n```{evaluation.strip()}```"
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(evaluation.strip()))
        await client.send_document(
            message.chat.id,
            document=filename,
            caption=f"► **INPUT:**\n`{cmd[0:980]}`\n\n► **OUTPUT:**\n`Attached Document`",
            reply_to_message_id=message.message_id
        )
        os.remove(filename)
    else:
        await edit_or_reply(message, text=final_output)