# Utility functions for podcast-tagger
# Add shared helpers here.

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


import os
import re


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