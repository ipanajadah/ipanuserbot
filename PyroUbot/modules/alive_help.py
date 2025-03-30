import random
import re
import os
import platform
import subprocess
import sys
import traceback
from datetime import datetime
from io import BytesIO, StringIO
from PyroUbot.config import OWNER_ID
import psutil
from PyroUbot import *
from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import *

from PyroUbot import *


@PY.UBOT("alive")
@PY.TOP_CMD
async def _(client, message):
    try:
        x = await client.get_inline_bot_results(
            bot.me.username, f"alive {message.id} {client.me.id}"
        )
        await message.reply_inline_bot_result(x.query_id, x.results[0].id, quote=True)
    except Exception as error:
        await message.reply(error)
    



@PY.INLINE("^alive")
async def _(client, inline_query):
    psr = await EMO.PASIR(client)
    get_id = inline_query.query.split()
    for my in ubot._ubot:
        if int(get_id[2]) == my.me.id:
            try:
                peer = my._get_my_peer[my.me.id]
                users = len(peer["pm"])
                group = len(peer["gc"])
            except Exception:
                users = random.randrange(await my.get_dialogs_count())
                group = random.randrange(await my.get_dialogs_count())
            get_exp = await get_expired_date(my.me.id)
            exp = get_exp.strftime("%d-%m-%Y") if get_exp else "None"
            if my.me.id in await get_list_from_vars(client.me.id, "ULTRA_PREM"):
                status = "SuperUltra"
            else:
                status = "Premium"
            button = BTN.ALIVE(get_id)
            start = datetime.now()
            await my.invoke(Ping(ping_id=0))
            ping = (datetime.now() - start).microseconds / 1000
            uptime = await get_time((time() - start_time))
            psr = await EMO.PASIR(client)
            msg = f"""
<blockquote>⌬ {bot.me.mention}
ᚗ status: {status} 
ᚗ {psr} expired_on: {exp} 
ᚗ dc_id: {my.me.dc_id}
ᚗ ping_dc: {ping} ms
ᚗ peer_users: {users} users
ᚗ peer_group: {group} group
ᚗ start_uptime: {uptime}</blockquote>
        <blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ɪᴘᴀɴ ࿈ᣄ</b></blockquote>
"""
            await client.answer_inline_query(
                inline_query.id,
                cache_time=300,
                results=[
                    (
                        InlineQueryResultArticle(
                            title="♅",
                            reply_markup=InlineKeyboardMarkup(button),
                            input_message_content=InputTextMessageContent(msg),
                        )
                    )
                ],
            )


@PY.CALLBACK("alv_cls")
async def _(client, callback_query):
    get_id = callback_query.data.split()
    if not callback_query.from_user.id == int(get_id[2]):
        return
    unPacked = unpackInlineMessage(callback_query.inline_message_id)
    for my in ubot._ubot:
        if callback_query.from_user.id == int(my.me.id):
            await my.delete_messages(
                unPacked.chat_id, [int(get_id[1]), unPacked.message_id]
            )


@PY.BOT("anu")
@PY.ADMIN
async def _(client, message):
    buttons = BTN.BOT_MENU(message)
    sh = await message.reply("menu information", reply_markup=InlineKeyboardMarkup(buttons))
    

@PY.CALLBACK("balik")
async def _(client, callback_query):
    buttons = BTN.BOT_MENU(callback_query)
    sh = await callback_query.message.edit("MENU information", reply_markup=InlineKeyboardMarkup(buttons))

@PY.CALLBACK("reboot")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id not in await get_list_from_vars(client.me.id, "ADMIN_USERS"):
        return await callback_query.answer("tombol ini bukan untuk lu", True)
    await callback_query.answer("system berhasil di restart", True)
    subprocess.call(["bash", "start.sh"])

@PY.CALLBACK("update")
async def _(client, callback_query):
    out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
    user_id = callback_query.from_user.id
    if not user_id == OWNER_ID:
        return await callback_query.answer("tombol ini bukan untuk lu", True)
    if "Already up to date." in str(out):
        return await callback_query.answer("ꜱudah terupdate", True)
    else:
        await callback_query.answer("ꜱedang memproꜱeꜱ update.....", True)
    os.execl(sys.executable, sys.executable, "-m", "userbot-ᴘʀᴇᴍ")


@PY.UBOT("menu")
async def user_help(client, message):
    if not get_arg(message):
        try:
            x = await client.get_inline_bot_results(bot.me.username, "user_menu")
            await message.reply_inline_bot_result(x.query_id, x.results[0].id)
        except Exception as error:
            await message.reply(error)
    else:
        module = (get_arg(message))
        if get_arg(message) in MENJ_COMMANDS:
            prefix = await ubot.get_prefix(client.me.id)
            await message.reply(
                MENU_COMMANDS[get_arg(message)].__MENU__.format(
                    next((p) for p in prefix)
                ),
                quote=True,
            )
        else:
            await message.reply(
                f"<b>⌭ No module found <code>{module}</code></b>"
            )

@PY.INLINE("^user_menu")
async def user_help_inline(client, inline_query):
    SH = await ubot.get_prefix(inline_query.from_user.id)
    msg = f"""<blockquote><b>𝗠 𝗘 𝗡 𝗨 𝗨 𝗦 𝗘 𝗥 𝗕 𝗢 𝗧</b>
<b> ∘ ᴜsᴇʀ: <a href=tg://user?id={inline_query.from_user.id}>{inline_query.from_user.first_name} {inline_query.from_user.last_name or ''}</a></b>
<b> ∘ ᴏᴡɴᴇʀ: @IPAN9Q</b>
<b> ∘ ᴘʟᴜɢɪɴs: {len(HELP_COMMANDS)}</b>
<b> ∘ ᴘʀᴇꜰɪxᴇs: {' '.join(SH)}</b></blockquote>"""
    results = [InlineQueryResultArticle(
        title="Menu Menu!",
        reply_markup=InlineKeyboardMarkup(paginate_modules(0, MENU_COMMANDS, "menu")),
        input_message_content=InputTextMessageContent(msg),
    )]
    await client.answer_inline_query(inline_query.id, cache_time=60, results=results)

@PY.CALLBACK("^close_user")
async def close_usernya(client, callback_query):
    unPacked = unpackInlineMessage(callback_query.inline_message_id)
    for x in ubot._ubot:
        if callback_query.from_user.id == int(x.me.id):
            await x.delete_messages(
                unPacked.chat_id, unPacked.message_id
            )

@PY.CALLBACK("menu_(.*?)")
async def help_callback(client, callback_query):
    mod_match = re.match(r"menu_module\((.+?)\)", callback_query.data)
    prev_match = re.match(r"menu_prev\((.+?)\)", callback_query.data)
    next_match = re.match(r"menu_next\((.+?)\)", callback_query.data)
    tutup_match = re.match(r"menu_tutup\((.+?)\)", callback_query.data)
    back_match = re.match(r"menu_back", callback_query.data)
    SH = await ubot.get_prefix(callback_query.from_user.id)
    top_text = f"""<blockquote><b>𝗠 𝗘 𝗡 𝗨 𝗨 𝗦 𝗘 𝗥 𝗕 𝗢 𝗧</b>
<b> ∘ ᴜsᴇʀ: <a href=tg://user?id={callback_query.from_user.id}>{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}</a></b>
<b> ∘ ᴏᴡɴᴇʀ: @IPAN9Q</b>
<b> ∘ ᴘʟᴜɢɪɴs: {len(HELP_COMMANDS)}</b>
<b> ∘ ᴘʀᴇꜰɪxᴇs: {' '.join(SH)}</b></blockquote>"""

    if mod_match:
        module = (mod_match.group(1)).replace(" ", "_")
        text = MENU_COMMANDS[module].__MENU__.format(next((p) for p in SH))
        button = [[InlineKeyboardButton("♅ ʙᴀᴄᴋ ♅", callback_data="menu_back")]]
        await callback_query.edit_message_text(
            text=text 
            + '\n<u><b>❕USERBOT 10K/BULAN BY @IPAN9Q</b></u>',
            reply_markup=InlineKeyboardMarkup(button),
            disable_web_page_preview=True,
        )
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(paginate_modules(curr_page - 1, MENU_COMMANDS, "menu")),
            disable_web_page_preview=True,
        )
    elif next_match:
        next_page = int(next_match.group(1))
        await callback_query.edit_message_text(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(paginate_modules(next_page + 1, MENU_COMMANDS, "menu")),
            disable_web_page_preview=True,
        )
    elif back_match:
        await callback_query.edit_message_text(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(paginate_modules(0, MENU_COMMANDS, "menu")),
            disable_web_page_preview=True,
        )
