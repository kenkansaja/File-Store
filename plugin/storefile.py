import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID")


@Client.on_message((filters.document|filters.video|filters.audio) & filters.incoming & ~filters.edited & ~filters.channel)
async def storefile(c, m):

    if m.document:
       media = m.document
    if m.video:
       media = m.video
    if m.audio:
       media = m.audio

    # text
    text = "--**Detail Berkas:**--\n\n\n"
    text += f"📂 __Nama Berkas:__ `{media.file_name}`\n\n"
    text += f"💽 __Tipe:__ `{media.mime_type}`\n\n"
    text += f"📊 __Ukuran Berkas:__ `{humanbytes(media.file_size)}`\n\n"
    if not m.document:
        text += f"🎞 __Durasi:__ `{TimeFormatter(media.duration * 1000)}`\n\n"
        if m.audio:
            text += f"🎵 __Judul:__ `{media.title}`\n\n"
            text += f"🎙 __Performa:__ `{media.performer}`\n\n" 
    text += f"__✏ Caption:__ `{m.caption}`\n\n"
    text += "**--Detail Upload:--**\n\n\n"
    text += f"__🦚 First Name:__ `{m.from_user.first_name}`\n\n"
    text += f"__🐧 Last Name:__ `{m.from_user.last_name}`\n\n" if m.from_user.last_name else ""
    text += f"__👁 User Name:__ @{m.from_user.username}\n\n" if m.from_user.username else ""
    text += f"__👤 User Id:__ `{m.from_user.id}`\n\n"

    # if databacase channel exist forwarding message to channel
    if DB_CHANNEL_ID:
        msg = await m.copy(int(DB_CHANNEL_ID))
        await msg.reply(text)

    # creating urls
    bot = await c.get_me()
    url = f"https://t.me/{bot.username}?start={m.chat.id}_{m.message_id}" if not DB_CHANNEL_ID else f"https://t.me/{bot.username}?start={m.chat.id}_{msg.message_id}"
    share_url = f"tg://share?url=File%20Link%20👉%20{url}"

    # making buttons
    buttons = [[
        InlineKeyboardButton(text="CEK 🔗", url=url),
        InlineKeyboardButton(text="SHARE 👤", url=share_url)
    ]]

    # sending message
    await m.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_message((filters.document|filters.video|filters.audio) & filters.incoming & filters.channel & ~filters.edited)
async def storefile_channel(c, m):

    if m.document:
       media = m.document
    if m.video:
       media = m.video
    if m.audio:
       media = m.audio

    # text
    text = "**DETAIL BERKAS:**\n\n\n"
    text += f"📂 __Nama Berkas:__ `{media.file_name}`\n\n"
    text += f"💽 __Tipe:__ `{media.mime_type}`\n\n"
    text += f"📊 __Ukuran Berkas:__ `{humanbytes(media.file_size)}`\n\n"
    if not m.document:
        text += f"🎞 __Durasi:__ `{TimeFormatter(media.duration * 1000)}`\n\n"
        if m.audio:
            text += f"🎵 __Judul:__ `{media.title}`\n\n"
            text += f"🎙 __Perfoma:__ `{media.performer}`\n\n"


    # if databacase channel exist forwarding message to channel
    if DB_CHANNEL_ID:
        msg = await m.copy(int(DB_CHANNEL_ID))
        await msg.reply(text)

    # creating urls
    bot = await c.get_me()
    url = f"https://t.me/{bot.username}?start={m.chat.id}_{m.message_id}" if not DB_CHANNEL_ID else f"https://t.me/{bot.username}?start={m.chat.id}_{msg.message_id}"
    share_url = f"tg://share?url={txt}File%20Link%20👉%20{url}"

    # making buttons
    buttons = [[
        InlineKeyboardButton(LINK="LINK 🔗", url=url),
        InlineKeyboardButton(SHARE="SHARE 👤", url=share_url)
    ]]

    # Editing and adding the buttons
    await m.edit_reply_markup(InlineKeyboardMarkup(buttons))


def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " days, ") if days else "") + \
        ((str(hours) + " hrs, ") if hours else "") + \
        ((str(minutes) + " min, ") if minutes else "") + \
        ((str(seconds) + " sec, ") if seconds else "") + \
        ((str(milliseconds) + " millisec, ") if milliseconds else "")
    return tmp[:-2]
