def test_sanity():
    assert True
 

from podcast_tagger.config import MP3_FOLDER

def test_mp3_folder_env_loaded():
    assert MP3_FOLDER is not None
    assert isinstance(MP3_FOLDER, str)
    assert len(MP3_FOLDER) > 0

from podcast_tagger.utils import detect_show_name

def test_detect_show_name_basic():
    folder = "/mnt/podcasts/SmartLess"
    assert detect_show_name(folder) == "SmartLess"

def test_detect_show_name_with_suffixes():
    assert detect_show_name("/mnt/SmartLess - New Batch") == "SmartLess"
    assert detect_show_name("/mnt/SmartLess (Live)") == "SmartLess"
    assert detect_show_name("/mnt/SmartLess [Remastered]") == "SmartLess"

import os
from importlib import reload
import podcast_tagger.config as config
from podcast_tagger.utils import detect_show_name

def test_env_to_show_name(monkeypatch):
    monkeypatch.setenv("MP3_FOLDER", "/mnt/podcasts/SmartLess - New Batch")
    reload(config)
    show_name = detect_show_name(config.MP3_FOLDER)
    assert show_name == "SmartLess"