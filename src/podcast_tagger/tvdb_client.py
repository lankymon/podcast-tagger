import requests
import json
from .config import (
    API_KEY, TVDB_LOGIN_URL, TVDB_SEARCH_URL, TVDB_SERIES_URL, JSON_PATH
)
from .utils import debug_log
def authenticate():
    response = requests.post(TVDB_LOGIN_URL, json={"apikey": API_KEY})
    response.raise_for_status()

    token = response.json()["data"]["token"]
    return {"Authorization": f"Bearer {token}"}

def fetch_series_id(headers, name):
    r = requests.get(
        TVDB_SEARCH_URL,
        params={"query": name, "type": "series"},
        headers=headers
    )
    r.raise_for_status()
    data = r.json().get("data", [])

    if not data:
        print(f"Warning: No TVDB match found for show name: '{name}'")
        return None

    return data[0]["tvdb_id"]
    


def fetch_episodes(headers, series_id):
    r = requests.get(
        f"{TVDB_SERIES_URL}/{series_id}/episodes/official",
        headers=headers
    )
    r.raise_for_status()

    eps = r.json()["data"]["episodes"]
    episode_list = []
    counter = 1

    for ep in eps:
        episode_list.append({
            "number": counter,
            "season": ep.get("seasonNumber"),
            "episode": ep.get("number"),
            "title": ep.get("name"),
            "date": ep.get("aired"),
            "type": ep.get("type"),
            "description": ep.get("overview"),
            "image": ep.get("image")
        })
        counter += 1

    return episode_list

def save_episode_json(episodes):
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump({"episodes": episodes}, f, indent=2)

def load_episode_json():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)["episodes"]