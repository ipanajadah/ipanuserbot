from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "gabut"
__HELP__ = """
<blockquote><b>✮ Bantuan Untuk gabut ✮

perintah : <code>{0}turbo</code>
    buat menjawab pertanyaan <code>{0}claude</code> haii</b></blockquote>
"""

async def costum_api(c, text, user_id):
    if user_id not in chat_topics:
        chat_topics[user_id] = [text]
    else:
        if isinstance(chat_topics[user_id], list):
            chat_topics[user_id].append(text)
        else:
            chat_topics[user_id] = [chat_topics[user_id], text]
    topik = chat_topics.get(user_id)[-1]
    gw = f"<a href=tg://user?id={c.me.id}>{c.me.first_name} {c.me.last_name or ''}</a>"
    bahan = [
        {
            "role": "system",
            "content": f"Lo adalah asisten telegram dari pengguna akun {gw}",
        },
        {
            "role": "assistant",
            "content": f"Lo adalah asisten telegram dari pengguna akun {gw} gunakan bahasa Indonesia toxic lo gw, anj, mmg, kntl, bacot serta gausah sok asik dan gausah menjelaskan apapun tugas lo hanya membalas pesan dengan singkat.",
        },
        {"role": "user", "content": f"{topik}"},
    ]
    url = "https://api.botcahx.eu.org/api/search/openai-custom"
    payload = {"message": bahan, "apikey": f"{botcax_api}"}
    res = await fetch.post(url, json=payload)
    if res.status_code == 200:
        data = res.json()
        return data["result"]
    else:
        return f"{res.text}"


@PY.UBOT("ask")
@PY.TOP_CMD
async def _(client: nlx, message, _):
    em = Emojik(client)
    em.initialize()
    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply(_("enc_5").format(em.gagal))
    a = client.get_text(message)
    user_id = client.me.id
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    pong_, uptime_, owner_, ubot_, proses_, sukses_ = initial_ctext(client)
    prs = await message.reply_text(_("proses").format(em.proses, proses_))

    try:
        x = await costum_api(client, a, user_id)
        chat_topics[user_id] = a
        await prs.delete()
        return await message.reply(
            "{}{}".format(em.sukses, x), reply_to_message_id=message.id
        )
    except Exception as e:
        await prs.delete()
        return await message.reply(_("err").format(em.gagal, str(e)))


async def generate_real(c, text):
    url = f"https://itzpire.com/ai/realistic?prompt={text}"
    res = await fetch.get(url)
    if res.status_code == 200:
        data = res.json()
        file = data["result"]
        photo = f"iz_{c.me.id}.jpg"
        await c.bash(f"wget {file} -O {photo}")
        return photo
