import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# احصل على هذه القيمة من my.telegram.org/apps
API_ID = int(getenv("API_ID","8934899"))
API_HASH = getenv("API_HASH","bf3e98d2c351e4ad06946b4897374a1e")
SOURCE_PHOTO = getenv("SOURCE_PHOTO")
DEV_URL = getenv("DEV_URL","https://t.me/y_9ame")
UPDATES_URL = getenv("UPDATES_URL", "https://t.me/sorce_paris")
SUPPORT_URL = getenv("SUPPORT_URL","https://t.me/sorce_paris")
# احصل على الرمز الخاص بك من @BotFather على Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","7951183367:AAH_g8tiVSmmQsbm9xItt0p46pY7-VC7408")

# احصل على عنوان URL الخاص بـ Mongo من cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://muntazer:omsn@muntazer.s9q3q.mongodb.net/?retryWrites=true&w=majority&appName=muntazer")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 480))

# معرف الدردشة لمجموعة لتسجيل أنشطة الروبوت
LOGGER_ID = int(getenv("LOGGER_ID","-1002136390368"))

# احصل على هذه القيمة من @FallenxBot على Telegram بواسطة /id
OWNER_ID = int(getenv("OWNER_ID","1497253321"))
OWNER = int(getenv("OWNER","1497253321"))

# اسم تطبيق heroku الخاص بك
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# api heroku الخاص بك
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/aesarj/mu",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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"
)  # املأ هذا المتغير إذا كان مستودعك الأصلي خاصًا

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/sorce_paris")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sorce_paris")

# اضبط هذا على "صحيح" إذا كنت تريد أن يترك المساعد المحادثات تلقائيًا بعد فترة زمنية محددة
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT","")

CHANNEL_SUDO = getenv("CHANNEL_SUDO", "sorce_paris")
YAFA_NAME = getenv("YAFA_NAME", "قناة الاشتراك")
YAFA_CHANNEL = getenv("YAFA_CHANNEL", "https://t.me/sorce_paris")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/sorce_paris")
BOT_USERNAME = getenv("BOT_USERNAME", "y_9amezsVbot")

# احصل على هذه البيانات من https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# الحد الأقصى لجلب مسار قائمة التشغيل من روابط youtube وspotify وapple.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999"))

# حد حجم ملفات الصوت والفيديو في Telegram (بالبايت)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# احصل على جلسة Pyrogram v2 الخاصة بك من @StringFatherBot على Telegram
STRING1 = getenv("STRING_SESSION", "BAHAsB4AbLj8SuWsn3sUeAAEc5MzhdFugl-1PWgdi4J2-Uhxi9Wi9CSAKseyydqYZlsjgghUb8h0X46zzGqfW_cSO7sr4Qoqus6EwZX3a4YtCqGi99URfQCf6-PhxujnfcAhYs1SLCuL03JmuXSoUePFyxmHqaoFhVL39a8vI5u9mQ5pyy-qkkaCJh9YK010pMgrGyYME0K-PoBvILGjFcegw9LuwKE8JneTXavVkAW5MR--rz74bZwkxLN07clmUf9hM1w0xwyI6SKKkKW8xHYAjL6nt3A-SZUsCP0DaXC1WRE99gQFVmp1j-pxTUDsxzpfGxq_8QHVKQ-9whid2XpGYB-NpQAAAAHh8bwwAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/220034b1e9af0ee930981.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://telegra.ph/file/220034b1e9af0ee930981.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
