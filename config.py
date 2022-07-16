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
SESSION_NAME = getenv("SESSION_NAME", "BQAv3qi6fAkSmFUcfBmxP3-vLRIrq09FcH_1NaLWf1ptATdMMi4E4m-Np3mNaXISNJ-ubmiCiFILOMpiXWTJeiwHpVuvVrQr6lS_dLrrecsnPSsvoA-1WeswB3D8j44934UcN6E4ISpmttj8kIBQrfPoYZzBFBBlfbEl7oubx_C8cVr7M9AZt-mT17U1ixEvmr4aUbfDwyugTMN2RwpOWsPRRV56c_LTCYkTIJkgWeLs2bWwrnMOtBYmeSHYc9T3lYE2bSBwO09AYkAFqJ_BIFAi_1N6qoC54AwKsiL0FANVBuahqdEdhGJJ5HChQyHulmcPbmv52-rUoTd3PFJuxvGgAAAAAUjUMyQA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
BOT_IMG = getenv("BOT_IMG", "https://te.legra.ph/file/19094320f302a8b6decac.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5516833572").split()))
