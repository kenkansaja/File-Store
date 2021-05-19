import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from .commands import start
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_callback_query("help")
async def help_cb(c, m):
    await m.answer()

    # help text
    help_text = """**Ada yang bisa saya bantu?? 🧐**

★ Berikan saya file dan saya akan merubahnya menjadi link


**kamu juga bisa menambahkan saya di channel 😉**

★ Cukup jadikan saya admin dengan ijin edit. Saya akan mengupload ulang dengan menambahkan button url link"""

    # creating buttons
    buttons = [
        [
            InlineKeyboardButton('BERANDA 🔝', callback_data="home"),
        [
            InlineKeyboardButton('TUTUP ⛔', callback_data="close")
        ]
    ]

