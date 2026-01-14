import os
from .config import MP3_FOLDER
from .utils import detect_show_name
from .tvdb_client import (
    authenticate,
    fetch_series_id,
    fetch_episodes,
    save_episode_json,
    load_episode_json
)
from .tagger import match_episode, tag_and_rename
from .listennotes_client import ln_search_show, ln_get_podcast_episodes


def fallback_listennotes(show_name, filename):
    """Fallback metadata lookup using Listen Notes."""
    shows = ln_search_show(show_name)
    if not shows:
        print(f"Listen Notes: no show found for '{show_name}'.")
        return None

    podcast_id = shows[0]["id"]
    episodes = ln_get_podcast_episodes(podcast_id)

    # Match by filename substring inside episode title
    for ep in episodes:
        title = ep.get("title", "").lower()
        if filename.lower().replace(".mp3", "") in title:
            return {
                "title": ep.get("title"),
                "description": ep.get("description"),
                "episode_number": ep.get("episode_number"),
                "image": ep.get("image"),
                "pub_date": ep.get("pub_date_ms"),
            }

    print(f"Listen Notes: no episode match for '{filename}'.")
    return None


def process_folder():
    headers = authenticate()
    show_name = detect_show_name(MP3_FOLDER)

    # --- TVDB primary lookup ---
    series_id = fetch_series_id(headers, name=show_name)

    if not series_id:
        print(f"TVDB has no entry for '{show_name}'.")
        print("Falling back to Listen Notes…")
        series_id = None

    if series_id:
        episodes = fetch_episodes(headers, series_id)
        save_episode_json(episodes)
        episodes = load_episode_json()
    else:
        episodes = None  # TVDB unavailable

    # --- Process MP3 files ---
    for filename in os.listdir(MP3_FOLDER):
        if not filename.lower().endswith(".mp3"):
            continue

        filepath = os.path.join(MP3_FOLDER, filename)

        ep = None

        # Try TVDB episode match first
        if episodes:
            ep = match_episode(filename, episodes)

        # Fallback to Listen Notes if TVDB fails
        if not ep:
            print(f"No TVDB match for: {filename}")
            print("Trying Listen Notes…")
            ep = fallback_listennotes(show_name, filename)

        if not ep:
            print(f"No metadata found for: {filename}")
            continue

        tag_and_rename(filepath, ep)