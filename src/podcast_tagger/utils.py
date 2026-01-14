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