from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import app
from strings.filters import command
from config import SOURCE_PHOTO, DEV_URL, UPDATES_URL, SUPPORT_URL

@app.on_message(
    command(["المالك", "مطور", "المطور"])
)
async def mak(client: Client, message: Message):
    await message.reply_photo(
        photo=SOURCE_PHOTO,
        caption="𝐒𝐎𝗨𝐑𝐂𝐄 𝐏𝐀𝐑𝐈𝐒\n~ Dav .",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⦗ Dev ⦘", url="https://t.me/F_Q_1")],
                [
                    InlineKeyboardButton("⦗ Updates ⦘", url="https://t.me/y_9ame"),
                    InlineKeyboardButton("⦗ support ⦘", url="https://t.me/sorce_paris"),
                ],
            ]
        ),
    )
