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
IKLAN = os.environ.get("IKLAN")

@Client.on_message(filters.command('start') & filters.incoming & filters.private)
async def start(c, m, cb=False):
    owner = await c.get_users(int(OWNER_ID))
    owner_username = owner.username if owner.username
#start text
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
  await relpy.message(
      text = IKLAN
   )
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
            return await m.reply_text(f"🥴Maaf File anda bermasalah")

        caption = f"{msg.caption.markdown}\n\n\n" if msg.caption else ""

        if chat_id.startswith('-100'): #if file from channel
            channel = await c.get_chat(int(chat_id))
            caption += f"\n\n\n**--DETAIL UNGGAHAN:--**\n\n"
            caption += f"__📢 Nama Channel:__ `{channel.title}`\n\n"
            caption += f"__👤 Channel Id:__ `{channel.id}`\n\n"
            caption += f"__💬 Sumber:__ {channel.dc_id}\n\n"
            caption += f"__👁 Jumlah Anggota:__ {channel.members_count}\n\n" 

        else: #if file not from channel
            user = await c.get_users(int(chat_id))
            
            

        await msg.copy(m.from_user.id, caption=caption)


    else: # sending start message
        await m.reply_text(
            text=text,
            quote=False,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

@Client.on_message(filters.command('me') & filters.incoming & filters.private)
async def me(c, m):
    """ This will be sent when /me command was used"""

    me = await c.get_users(m.from_user.id)
    text = "--**YOUR DETAILS:**--\n\n\n"
    text += f"__🦚 First Name:__ `{me.first_name}`\n\n"
    text += f"__🐧 Last Name:__ `{me.last_name}`\n\n" if me.last_name else ""
    text += f"__👁 User Name:__ @{me.username}\n\n" if me.username else ""
    text += f"__👤 User Id:__ `{me.id}`\n\n"
    text += f"__💬 DC ID:__ {me.dc_id}\n\n" if me.dc_id else ""
    text += f"__✔ Is Verified By TELEGRAM:__ `{me.is_verified}`\n\n" if me.is_verified else ""
    text += f"__👺 Is Fake:__ {me.is_fake}\n\n" if me.is_fake else ""
    text += f"__💨 Is Scam:__ {me.is_scam}\n\n" if me.is_scam else ""
    text += f"__📃 Language Code:__ {me.language_code}\n\n" if me.language_code else ""

    await m.reply_text(text, quote=True)
