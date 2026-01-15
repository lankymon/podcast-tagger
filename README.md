# podcast-tagger

## Overview

**Podcast Tagger** is a metadata enrichment pipeline for podcast MP3 files. It retrieves episode information from multiple metadata providers, matches it to local audio files, and applies ID3 tags including title, episode number, description, and artwork.

Originally built for SmartLess episodes stored on a local NAS, the system now supports **automatic detection of any show** based on the folder name. This includes robust **regex‑based suffix stripping** (e.g., `(Live)`, `[Remastered]`, `- New Batch`) to ensure consistent show identification even when folder names vary.

---

## Multi‑Provider Metadata Chain

As of **0.3.0**, the pipeline uses a layered metadata strategy:

1. **TVDB** — primary metadata source
2. **Listen Notes** — fallback when TVDB has no series or missing episodes
3. **BBC Sounds (experimental)** — optional scraper for BBC‑exclusive shows, included as a scaffold for future use

This multi‑provider chain ensures reliable tagging even when a show is missing from one service.

---

## Setup

To create and activate the virtual environment and install dependencies:

```bash
./setup_env.ps1
```

Your `.env` file should contain:

```env
TVDB_API_KEY=your-tvdb-key
LISTEN_NOTES_API_KEY=your-listennotes-key
MP3_FOLDER=your-mp3-directory
```

> **Note:**  
> `MP3_FOLDER` should point to the directory containing your MP3 files.  
> The folder name is automatically parsed to detect the show name using regex‑based suffix stripping.

---

## Running Tests

Run the test suite with:

```bash
./run_tests.ps1
```

The tests cover:

- environment variable loading
- show‑name detection (including suffix variants)
- core pipeline behaviour

Integration tests for external APIs can be added separately.

---

## Notebooks

To launch Jupyter Lab inside the project environment:

```bash
./start_notebook.ps1
```

---

## Project Structure

- `src/podcast_tagger/` — source code modules
  - `core.py` — orchestration logic (show detection, metadata fetch, provider fallback, tagging pipeline)
  - `tvdb_client.py` — TVDB API integration
  - `listennotes_client.py` — Listen Notes API integration
  - `tagger.py` — MP3 tagging logic
  - `utils.py` — filename parsing and regex‑based show detection
  - `config.py` — environment‑driven configuration
  - `bbc_scraper.py` — experimental BBC Sounds scraper (persistent‑profile Playwright scaffold)
- `metadata/` — cached episode metadata (JSON)
- `notebooks/` — exploratory notebooks
- `datasets/` — project‑specific datasets (not synced)
- `scripts/` — helper scripts
- `main.py` — entry point for the tagging pipeline
- `.env` — environment variables (not committed)
- `requirements.txt` — Python dependencies

---

## Version History

This project follows semantic versioning.

- `0.1.0` — initial version
- `0.2.0` — dynamic show detection, regex suffix stripping, TVDB fallback, expanded debug logging
- **`0.3.0` — Listen Notes fallback provider, unified metadata structure, expanded multi‑provider architecture, BBC Sounds scraper scaffold**

---

## License

MIT License — see `LICENSE` for details.
