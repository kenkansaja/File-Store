import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID")
OWNER_ID = os.environ.get("OWNER_ID")


@Client.on_message(filters.command('start') & filters.incoming & filters.private)
async def start(c, m, cb=False):
    owner = await c.get_users(int(OWNER_ID))
    owner_username = owner.username if owner.username else 'Ns_bot_updates'

    # start text
    text = f"""Hay {m.from_user.mention(style='md')}

Saya adalah bot pembuat link permanen dari berkas yang kamu kirim 📂.


"""

    # Buttons
    buttons = [
           [
            InlineKeyboardButton('📝 BANTUAN 📝', callback_data="help"),
            InlineKeyboardButton('⛔ TUTUP ⛔', callback_data="close")
       ]
    ]

    # when button home is pressed
    if cb:
        return await m.message.edit(
                   text=text,
                   reply_markup=InlineKeyboardMarkup(buttons)
               )

    if len(m.command) > 1: # sending the stored file
        chat_id, msg_id = m.command[1].split('_')
        msg = await c.get_messages(int(chat_id), int(msg_id)) if not DB_CHANNEL_ID else await c.get_messages(int(DB_CHANNEL_ID), int(msg_id))

        if msg.empty:
            owner = await c.get_users(int(OWNER_ID))
            return await m.reply_text(f"🥴 Maaf File anda bermasalah")

        caption = f"{msg.caption.markdown}\n\n\n" if msg.caption else ""

        if chat_id.startswith('-100'): #if file from channel
            channel = await c.get_chat(int(chat_id))
            caption += "\n\n\n**--DETAIL UNGGAHAN:--**\n\n"
            caption += f"__📢 Nama Channel:__ `{channel.title}`\n\n"
            caption += f"__👤 Channel Id:__ `{channel.id}`\n\n"
            caption += f"__💬 Sumber:__ {channel.dc_id}\n\n"
            caption += f"__👁 Jumlah Anggota:__ {channel.members_count}\n\n" 

        else: #if file not from channel
            user = await c.get_users(int(chat_id))
            caption += "\n\n\n**--DETAIL UNGGAHAN:--**\n\n"
            caption += f"__💬 SUMBER:__ {user.dc_id}\n\n"

        await msg.copy(m.from_user.id, caption=caption)


    else: # sending start message
        await m.reply_text(
            text=text,
            quote=False,
            reply_markup=InlineKeyboardMarkup(buttons)
        )


@Client.on_message(filters.command('me') & filters.incoming & filters.private)
async def me(c, m):
    me = await c.get_users(m.from_user.id)
    text = "--**DETAIL KAMU:**--\n\n\n"
    text += f"__💬 DC ID:__ {me.dc_id}\n\n"
    text += f"__✔ VERIFIKASI TELEGRAM:__ `{me.is_verified}`\n\n"
    text += f"__👺 INI PALSU:__ {me.is_fake}\n\n"
    text += f"__💨 INI SCAM:__ {me.is_scam}\n\n"
    text += f"__📃 KODE BAHASA:__ {me.language_code}\n\n"

    await m.reply_text(text, quote=True
)
