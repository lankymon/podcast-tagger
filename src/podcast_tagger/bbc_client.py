import re
from .utils import load_bbc_urls, parse_filename_tokens
from .bbc_scraper import fetch_bbc_sounds_episodes


def match_bbc_episode(filename, episodes):
    tokens = parse_filename_tokens(filename)

    best_match = None
    best_score = 0

    for ep in episodes:
        title = (ep.get("title") or "").lower()
        words = re.findall(r"[a-z]+", title)

        score = sum(1 for t in tokens if t in words)

        if score > best_score:
            best_score = score
            best_match = ep

    return best_match if best_score >= 2 else None


def fallback_bbc(show_name, filename):
    urls = load_bbc_urls()
    bbc_url = urls.get(show_name)

    if not bbc_url:
        print("BBC Sounds: no URL available for this show.")
        return None

    try:
        data = fetch_bbc_sounds_episodes(bbc_url)
    except Exception as e:
        print("BBC Sounds scraping unavalable on this system:", e)
        return None

    episodes = data.get("episodes", [])
    print("DEBUG: BBC returned", len(episodes), "episodes")

    if not episodes:
        print("BBC Sounds: no episodes found.")
        return None

    ep = match_bbc_episode(filename, episodes)
    if not ep:
        print(f"BBC Sounds: no episode match for '{filename}'.")
        return None

    return {
        "title": ep["title"],
        "description": ep["description"],
        "episode_number": ep["number"],
        "image": ep["image"],
        "pub_date": ep["date"],
    }