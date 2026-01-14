import os
import time
import requests
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TDRC, COMM, APIC, TRCK
from mutagen.mp3 import MP3

from .utils import clean_filename, strip_edge_underscores, normalise
from .config import MP3_FOLDER

def match_episode(filename, episodes):
    cleaned = strip_edge_underscores(filename)
    base = os.path.splitext(cleaned)[0]
    match_key = normalise(base)

    best = None
    best_score = 0

    for ep in episodes:
        title_norm = normalise(ep["title"])

        if title_norm and match_key in title_norm:
            return ep

        score = sum(c in title_norm for c in match_key)
        if score > best_score:
            best_score = score
            best = ep

    return best

def tag_and_rename(filepath, episode):
    filename = os.path.basename(filepath)
    safe_title = clean_filename(episode["title"])
    new_name = f"{episode['number']:03d} - {safe_title}.mp3"
    new_path = os.path.join(MP3_FOLDER, new_name)

    if os.path.exists(new_path):
        print(f"Already processed: {new_name}")
        return

    for _ in range(3):
        try:
            audio = MP3(filepath)
            break
        except Exception:
            time.sleep(1)
    else:
        print("Persistent failure", filepath)
        return

    audio = MP3(filepath, ID3=ID3)
    try:
        audio.add_tags()
    except:
        pass

    audio["TIT2"] = TIT2(encoding=3, text=episode["title"] or "")
    audio["TALB"] = TALB(encoding=3, text="SmartLess")
    audio["TPE1"] = TPE1(encoding=3, text="SmartLess")
    audio["TDRC"] = TDRC(encoding=3, text=episode["date"] or "")
    audio["TRCK"] = TRCK(encoding=3, text=str(episode["number"]))

    desc = episode.get("description")
    if desc:
        audio["COMM"] = COMM(encoding=3, lang="eng", desc="desc", text=desc)

    image_url = episode.get("image")
    if image_url:
        if image_url.startswith("/"):
            image_url = "https://artworks.thetvdb.com" + image_url

        try:
            img_data = requests.get(image_url).content
            audio["APIC"] = APIC(
                encoding=3,
                mime="image/jpeg",
                type=3,
                desc="Cover",
                data=img_data
            )
        except:
            print("Image fetch failed, skipping artwork")

    audio.save()
    os.rename(filepath, new_path)
    print(f"{filename} → Renamed to: {new_name}")