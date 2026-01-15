# Utility functions for podcast-tagger
# Add shared helpers here.

import os
import re
import json


def clean_filename(name):
    illegal = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in illegal:
        name = name.replace(char, '')
    return name.strip()


def strip_edge_underscores(name):
    return name.strip('_')


def normalise(text):
    if not text:
        return ""
    return (
        text.lower()
        .replace(" ", "")
        .replace("-", "")
        .replace("_", "")
        .replace(":", "")
        .replace("!", "")
        .replace("’", "")
        .replace("'", "")
    )


def detect_show_name(folder_path):
    """Extract show name from folder path, stripping suffixes like:
       - ' - New Batch'
       - '(Live)'
       - '[Remastered]'
    """
    base = os.path.basename(folder_path)

    # Strip parentheses suffixes: (Live), (Encore), (2024)
    base = re.sub(r"\s*\([^)]*\)$", "", base)

    # Strip bracket suffixes: [Remastered], [2024]
    base = re.sub(r"\s*\[[^\]]*\]$", "", base)

    # Strip dash suffixes: - New Batch, - Max Batch, - Archive
    base = re.sub(r"\s*-\s.*$", "", base)

    return base.strip()


def debug_log(message):
    
    with open("debug.log", "a", encoding="utf-8") as f:
        f.write(message + "\n")


def load_bbc_urls():
    path = os.path.join(os.path.dirname(__file__), "bbc_urls.json")
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def parse_filename_tokens(filename):
    base = filename.lower().replace(".mp3", "")
    parts = re.split(r"[-_]|(?=[A-Z])", base)

    tokens = [p for p in parts if p]

    final = []
    for t in tokens:
        final.extend(re.findall(r"[a-z]+", t.lower()))

    return final