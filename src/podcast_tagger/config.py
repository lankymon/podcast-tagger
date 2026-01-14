import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TVDB_API_KEY", "")
MP3_FOLDER = os.getenv("MP3_FOLDER", "")

JSON_PATH = "data/external/smartless.json"

TVDB_LOGIN_URL = "https://api4.thetvdb.com/v4/login"
TVDB_SEARCH_URL = "https://api4.thetvdb.com/v4/search"
TVDB_SERIES_URL = "https://api4.thetvdb.com/v4/series"