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

def process_folder():
    headers = authenticate()
    show_name = detect_show_name(MP3_FOLDER)
    series_id = fetch_series_id(headers, name=show_name)

    if not series_id:
        print(f"TVDB has no entry for '{show_name}'.")
        print("Skipping metadata fetch.")
        return
    episodes = fetch_episodes(headers, series_id)
    save_episode_json(episodes)

    episodes = load_episode_json()

    for filename in os.listdir(MP3_FOLDER):
        if not filename.lower().endswith(".mp3"):
            continue

        filepath = os.path.join(MP3_FOLDER, filename)
        ep = match_episode(filename, episodes)

        if not ep:
            print(f"No match for: {filename}")
            continue

        tag_and_rename(filepath, ep)