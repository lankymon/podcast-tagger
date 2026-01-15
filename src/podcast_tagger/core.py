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
from .listennotes_client import fallback_listennotes
from .bbc_client import fallback_bbc



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

        # Fallback to BBC Sounds if Listen Notes fails
        if not ep:
            print("Trying BBC Sounds…")
            ep = fallback_bbc(show_name, filename)

        if not ep:
            print(f"No metadata found for: {filename}")
            continue

        tag_and_rename(filepath, ep)