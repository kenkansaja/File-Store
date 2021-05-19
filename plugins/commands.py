import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command('start') & filters.incoming & filters.private)
async def start(c, m, cb=True):
    
    # start text
    text = f"""Hey! {m.from_user.mention(style='md')}

💡 ** Saya adalah Bot File Store **

`Kamu dapat mengirimkan saya media atau file, Dan saya akan mengubahnya menjadi link permanen`
"""
    # when button home is pressed
    if cb:
        return await m.message.edit(
                   text=text,
                   reply_markup=InlineKeyboardMarkup(buttons)
               )

    
    else: # sending start message
        await m.reply_text(
            text=text,
            quote=True,
            reply_markup=InlineKeyboardMarkup(buttons)
        )


@Client.on_message(filters.command('me') & filters.private)
async def me(c, m):
      await m.reply_text(text, quote=True)
