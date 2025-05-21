from pyrogram import Client, filters
from pyrogram.types import Message
from AnonXMusic import app
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


@app.on_message(
    command(["السورس", "سورس", "المبرمج"])
)
async def mak(client: Client, message: Message):
    await message.reply_photo(
        photo="https://j.top4top.io/p_34280arr60.jpg",
        caption="𝐒𝐎𝗨𝐑𝐂𝐄 𝐏𝐀𝐑𝐈𝐒\n~ Dav Source",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⦗ ⁨⁩𝙃𝙀𝙇𝙇𝘼𝙎 ⦘", url="https://t.me/F_Q_1"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "⦗ ⁨𝗞𝗮𝗿𝗮𝘀𝗼⁩ ⦘", url="https://t.me/y_9ame"
                    ),
                    InlineKeyboardButton(
                        "⦗ 𝐒𝐎𝗨𝐑𝐂𝐄 𝐏𝐀𝐑𝐈𝐒 ⦘", url="https://t.me/sorce_paris"
                    ),
                ],
            ]
        ),
    )
