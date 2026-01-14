import os
from importlib import reload
from podcast_tagger.config import MP3_FOLDER
from podcast_tagger.utils import detect_show_name
import podcast_tagger.config as config


def test_sanity():
    assert True


def test_mp3_folder_env_loaded():
    assert MP3_FOLDER is not None
    assert isinstance(MP3_FOLDER, str)
    assert len(MP3_FOLDER) > 0


def test_detect_show_name_basic():
    folder = "/mnt/podcasts/SmartLess"
    assert detect_show_name(folder) == "SmartLess"


def test_detect_show_name_with_suffixes():
    assert detect_show_name("/mnt/SmartLess - New Batch") == "SmartLess"
    assert detect_show_name("/mnt/SmartLess - Max Batch") == "SmartLess"
    assert detect_show_name("/mnt/SmartLess (Live)") == "SmartLess"
    assert detect_show_name("/mnt/SmartLess [Remastered]") == "SmartLess"
    assert detect_show_name("/mnt/SmartLess (Encore)") == "SmartLess"
    assert detect_show_name("/mnt/SmartLess - Archive") == "SmartLess"
    assert detect_show_name("/mnt/SmartLess [2024]") == "SmartLess"


def test_env_to_show_name(monkeypatch):
    monkeypatch.setenv("MP3_FOLDER", "/mnt/podcasts/SmartLess (Live)")
    reload(config)
    show_name = detect_show_name(config.MP3_FOLDER)
    assert show_name == "SmartLess"