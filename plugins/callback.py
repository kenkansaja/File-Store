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

    # editing as help message
    await m.message.edit(
        text=help_text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_callback_query('close')
async def close_cb(c, m):
    await m.message.delete()
    await m.message.reply_to_message.delete()

    # editing message
    await m.message.edit(
        text=about_text,
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )


@Client.on_callback_query("home")
async def home_cb(c, m):
    await m.answer()
    await start(c, m, cb=True)
