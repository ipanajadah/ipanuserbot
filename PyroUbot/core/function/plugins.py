import importlib
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PyroUbot import bot, ubot
from PyroUbot.core.helpers import PY
from PyroUbot.modules import loadModule
from PyroUbot.core.database import *
from PyroUbot.config import OWNER_ID
from platform import python_version
from pyrogram import __version__
HELP_COMMANDS = {}


async def loadPlugins():
    modules = loadModule()
    for mod in modules:
        imported_module = importlib.import_module(f"PyroUbot.modules.{mod}")
        module_name = getattr(imported_module, "MODULE", "").replace(" ", "_").lower()
        if module_name:
            HELP_COMMANDS[module_name] = imported_module
    print(f"[🤖 ᴜsᴇʀʙᴏᴛ 🤖] [💠 TELAH BERHASIL DIAKTIFKAN! 💠]")
    await bot.send_message(
        LOGS_MAKER_UBOT, 
       f"""                    
<blockquote>🤖 ᴜsᴇʀʙᴏᴛ ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋᴛɪꜰᴋᴀɴ</b>

<b>👤Userbot: {len(ubot._ubot)}</b>
<b>🤖ᴍᴏᴅᴜʟᴇs: {len(HELP_COMMANDS)}</b>
<b>📘ᴘʏᴛʜᴏɴ: {python_version()}</b>
<b>📙ᴘʏʀᴏɢʀᴀᴍ: {__version__}</blockquote> 
""",
   reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("LIST USERBOT 🤖", callback_data="cek_ubot"),
                ],
            ]
        ),
                          )
    
@PY.CALLBACK("0_cls")
async def _(client, callback_query):
    await callback_query.message.delete()
