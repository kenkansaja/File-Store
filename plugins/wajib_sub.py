from bot import WAJIB_SUB
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def handle_force_sub(bot, cmd):
    invite_link = await bot.create_chat_invite_link(int(WAJIB_SUB))
    try:
        user = await bot.get_chat_member(int(WAJIB_SUB), cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="Maaf Tuan anda telah masuk daftar baned. Silahkan kontak [Support Group](https://t.me/musikkugroup).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Tolong join dulu di group atau channel kami!**\n\nAgar bisa menggunakan bot ini!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Join dulu bos", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshmeh")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Sepertinya ada yang salah silahkan hubungi! [Support Group](https://t.me/musikkugroup).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
