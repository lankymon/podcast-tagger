import os

# Load .env manually
def load_env_file(path=".env"):
    if not os.path.exists(path):
        print(f"Warning: {path} not found.")
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip())

# Load environment variables
load_env_file()

# Access config values
API_KEY = os.getenv("TVDB_API_KEY", "")
MP3_FOLDER = os.getenv("MP3_FOLDER", "")

# Constants
JSON_PATH = "data/external/smartless.json"
TVDB_LOGIN_URL = "https://api4.thetvdb.com/v4/login"
TVDB_SEARCH_URL = "https://api4.thetvdb.com/v4/search"
TVDB_SERIES_URL = "https://api4.thetvdb.com/v4/series"