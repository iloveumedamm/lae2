# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv("API_ID", "26305247"))
    API_HASH = str(getenv("API_HASH",  "20ca7e6687c281e11782856c7efd0ff7"))
    BOT_TOKEN = str(getenv("BOT_TOKEN", "6257817586:AAHiHfYz_Ykn_n1QHgE7o1aRdOn5Gxg6M4U"))
    name = str(getenv("name", "filetolinkbot"))
    SLEEP_THRESHOLD = int(getenv("SLEEP_THRESHOLD", "60"))
    WORKERS = int(getenv("WORKERS", "4"))
    BIN_CHANNEL = int(getenv("BIN_CHANNEL", "-1001853354560"))
    PORT = int(getenv("PORT", 8000))
    BIND_ADRESS = str(getenv("WEB_SERVER_BIND_ADDRESS", "178.128.207.223"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5791145987").split())
    NO_PORT = bool(getenv("NO_PORT", "80"))
    APP_NAME = None
    OWNER_USERNAME = str(getenv("OWNER_USERNAME", "Ipapcornbot_Owner"))
    if "DYNO" in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv("APP_NAME"))

    else:
        ON_HEROKU = False
    FQDN = str(getenv("FQDN", BIND_ADRESS)) if not ON_HEROKU or getenv("FQDN") else APP_NAME + ".herokuapp.com"
    HAS_SSL = bool(getenv("HAS_SSL", False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv("DATABASE_URL", "mongodb+srv://W9Uyj61afEXSw601:W9Uyj61afEXSw601@cluster0.zsxso.mongodb.net/?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(getenv("UPDATES_CHANNEL", "latvefg"))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))
