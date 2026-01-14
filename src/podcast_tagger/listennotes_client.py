import os
import requests

LISTEN_NOTES_API_KEY = os.getenv("LISTEN_NOTES_API_KEY")
BASE_URL = "https://listen-api.listennotes.com/api/v2"

HEADERS = {
    "X-ListenAPI-Key": LISTEN_NOTES_API_KEY
}


def ln_search_show(show_name: str):
    """Search Listen Notes for a show by name."""
    url = f"{BASE_URL}/search"
    params = {"q": show_name, "type": "podcast"}
    r = requests.get(url, params=params, headers=HEADERS)
    r.raise_for_status()
    data = r.json()
    return data.get("results", [])


def ln_get_podcast_episodes(podcast_id: str):
    """Fetch all episodes for a podcast."""
    url = f"{BASE_URL}/podcasts/{podcast_id}"
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    return r.json().get("episodes", [])