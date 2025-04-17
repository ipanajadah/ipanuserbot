from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import OWNER_ID, bot, ubot, get_expired_date


class MSG:     
    def EXP_MSG_UBOT(X):
        return f"""
<blockquote><b>❏ ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ ɪᴅ:</b> <code>{X.me.id}</code>
<b>╰ ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴛᴇʟᴀʜ ʜᴀʙɪs</b></blockquote>
"""

    def START(message):
        return f"""
</b>𝙊𝙇𝘼  <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a></b>
 
<blockquote><b>📚 {bot.me.mention} 𝙄𝙉𝙄 𝘼𝘿𝘼𝙇𝘼𝙃 𝘽𝙊𝙏 𝙐𝙇𝙏𝙍𝘼 𝙋𝙍𝙀𝙈</b>

<blockquote><b>𝙄𝙉𝙄 𝘼𝘿𝘼𝙇𝘼𝙃 𝘽𝙊𝙏 𝙈𝙐𝙇𝙏𝙄𝙁𝙐𝙉𝙂𝙎𝙄 𝙔𝘼𝙉𝙂 𝘿𝙄 𝘽𝙐𝘼𝙏 𝙊𝙇𝙀𝙃 𝙊𝙒𝙉𝙀𝙍 𝙆𝙐 𝙔𝘼𝙄𝙏𝙐 @Ipannzzzzx 
𝙅𝙄𝙆𝘼 𝙄𝙉𝙂𝙄𝙉 𝘽𝙀𝙍𝙏𝘼𝙉𝙔𝘼² 𝘽𝙄𝙎𝘼 𝙇𝘼𝙉𝙂𝙎𝙐𝙉𝙂 𝙆𝙀 𝘾𝙃𝘼𝙏 𝙋𝙑 𝙔𝘼 𝙂𝙐𝙔𝙎</b>


<blockquote><b>𝙅𝙄𝙆𝘼 𝙄𝙉𝙂𝙄𝙉 𝙈𝙀𝙈 𝘽𝙀𝙇𝙄 𝘽𝙄𝙎𝘼 𝘾𝙇𝙄𝙆 𝘽𝙐𝙏𝙊𝙉 𝘿𝙄 𝘽𝘼𝙒𝘼𝙃 👇</b>"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<blockquote><b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>

<b>⎆ ᴍᴏᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:</b>
 <b>├ 𝙶𝙾𝙿𝙰𝚈​ </𝚋>
 <b>├────• 08𝟻𝟽𝟻𝟶𝟷𝟶𝟽𝟻𝟶𝟻</b>
 <b>├────•  SY***</b>
 <b>├ 𝙳𝙰𝙽𝙰 </b>
 <b>├────• 𝟶𝟾𝟻𝟽𝟻𝟶𝟷𝟶𝟽𝟻𝟶𝟻</b>
 ᴜɴᴛᴜᴋ ᴍᴇᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ʟᴀɪɴɴʏᴀ ʙɪꜱᴀ ʟᴀɴɢꜱᴜɴɢ ʜᴜʙ ᴏᴡɴᴇʀ, ᴀᴅᴍɪɴ ᴅᴀɴ sᴇʟᴇʀ.

<b>⌭ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b></blockquote>
"""

    async def UBOT(count):
        return f"""
<blockquote><b>⌬ ᴜsᴇʀʙᴏᴛ ᴋᴇ</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b> ├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b> ╰ ɪᴅ:</b> <code>{ubot._ubot[int(count)].me.id}</code></blockquote>
"""

    def POLICY():
        return """
ʙᴜᴀᴛ ʏᴀɴɢ ɴᴀɴʏᴀ ᴘᴇɴɢɢᴜɴᴀᴀɴ ᴜsᴇʀʙᴏᴛ ʏᴀɴɢ ᴀᴍᴀɴ ʙᴜᴀᴛ ᴅɪ ᴘᴀsᴀɴɢ ᴅɪ ᴀᴋᴜɴ ɪᴅ ᴀᴡᴀʟᴀɴ ʙᴇʀᴀᴘᴀ ʏᴀ??
ɢɪɴɪ ᴜɴᴛᴜᴋ ᴘᴇɴɢɢᴜɴᴀ ᴜsᴇʀʙᴏᴛ ɪᴛᴜ ᴊᴀɴɢᴀɴ ᴘᴇɴɢɢᴜɴᴀ ɪᴅ ᴀᴡᴀʟᴀɴ 𝟼-𝟽 ᴋᴀʀɴᴀ sᴀɴɢᴀᴛ ʀᴀᴡᴀɴ ᴊɪᴋᴀ ᴅɪ ᴘᴀsᴀɴɢ ᴜsᴇʀʙᴏᴛ.
ᴜɴᴛᴜᴋ ᴘᴇᴍᴀᴋᴀɪᴀɴ ᴜsᴇʀʙᴏᴛ ʙɪᴀsᴀ ᴅɪ ᴘᴀᴋᴀɪ ᴅɪ ᴀᴋᴜɴ ʟᴀᴍᴀ ᴀᴛᴀᴜ ʙɪᴀsᴀ ɪᴅ ᴀᴡᴀʟᴀɴ 𝟷-𝟻,
sᴇᴍᴜᴀ ᴘᴇɴɢɢᴜɴᴀ ᴅᴀʀɪ ɪᴅ ᴛᴇʀsᴇʙᴜᴛ sᴜᴅᴀʜ ᴛᴇʀʙɪʟᴀɴɢ ᴀᴍᴀɴ ᴛᴀᴘɪ sᴇᴍᴜᴀ ᴛᴇʀɢᴀɴᴛᴜɴɢ ᴘᴇᴍᴀᴋᴀɪᴀɴ ᴋᴀʟɪᴀɴ.
"""
