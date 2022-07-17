# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚

from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "9194842"))
API_HASH = getenv("API_HASH", "73a311feefa9a6dd437d3ae9bd4f8cbb")
BOT_TOKEN = getenv("BOT_TOKEN", "5515309267:AAH3O_AnzyEgY5DPKa3COReNML3d2I8sezY")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Op_cutearnav123")
BOT_USERNAME = getenv("BOT_USERNAME", "arnav_officialbot")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Final_Countdown_Survivors")
BOT_NAME = getenv("BOT_NAME","ᴀʀɴᴀᴠ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ🥀")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))
SESSION_NAME = getenv("SESSION_NAME", "BQCHFqkL5KObbWkkQOX8XjJ4hG-dpB_gGcoJf9PloZQXOyQVYh9SZfNleooApCXL81L692scMOYOEEc2s_utJhp3y6CD_FC5QI36Z5p9aS7wOwoHSX1gjtmAQrc4dAqie5nkW0mlF862vlUKgBzBenuBLklrzqfGAS4PK18FQ-hdzaFhUVRAdx0fT4_Pi3RFpPWKg1h_7ZhXQwBJcz_GZ9xPd25det8rWlEWQft4uKaJdN0Yg29yGKlcysxOuP1kLXHBcWOOIU1XuR78I1-yXRnsh1D1R3xH_PHvVazcNmgX7SF_PEk-gdNCmQ-hilyNT8S1XXxYBIDzLloOBBrQvyU2AAAAAUjUMyQA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
BOT_IMG = getenv("BOT_IMG", "https://te.legra.ph/file/19094320f302a8b6decac.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5516833572").split()))
