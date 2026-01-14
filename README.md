# podcast-tagger

## Overview

Podcast Tagger is a metadata enrichment pipeline for podcast MP3 files. It fetches episode data from multiple metadata providers, matches it to local audio files, and applies ID3 tags including title, episode number, description, and artwork.

Originally designed for SmartLess episodes stored on a local NAS, the system now supports **dynamic detection of any show** based on the folder name. This includes robust **regex‑based stripping of suffixes** such as `(Live)`, `[Remastered]`, and `- New Batch`, ensuring consistent show identification even when folder names vary.

### Multi‑Provider Metadata Chain

As of version **0.3.0**, the pipeline uses a layered metadata strategy:

1. **TVDB** — primary provider
2. **Listen Notes** — fallback when TVDB has no series or missing episodes
3. _(Future)_ BBC Sounds scraping for BBC‑exclusive shows

This ensures reliable tagging even when a show is missing from one provider.

---

## Setup

To create and activate the virtual environment and install dependencies:

```bash
./setup_env.ps1
```

Ensure your `.env` file contains:

```env
TVDB_API_KEY=your-tvdb-key
LISTEN_NOTES_API_KEY=your-listennotes-key
MP3_FOLDER=your-mp3-directory
```

> **Note:**  
> `MP3_FOLDER` should point to the folder containing the MP3 files.  
> The folder name is automatically parsed to detect the show name using regex‑based suffix stripping.

---

## Running Tests

To run the test suite:

```bash
./run_tests.ps1
```

The tests include:

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

- `src/podcast_tagger/` – source code modules
  - `core.py` – orchestration logic (show detection, metadata fetch, provider fallback, tagging pipeline)
  - `tvdb_client.py` – TVDB API integration
  - `listennotes_client.py` – Listen Notes API integration (fallback provider)
  - `tagger.py` – MP3 tagging logic
  - `utils.py` – filename and string helpers (including regex‑based show name detection)
  - `config.py` – environment‑driven configuration
- `metadata/` – serialized JSONs (cached episode metadata)
- `notebooks/` – exploratory notebooks
- `datasets/` – project‑specific datasets (not synced)
- `scripts/` – helper scripts
- `main.py` – entry point for the tagging pipeline
- `.env` – environment variables (not committed)
- `requirements.txt` – Python dependencies

---

## Version

This project follows semantic versioning.

- `0.1.0` — initial version
- `0.2.0` — dynamic show detection, regex suffix stripping, TVDB fallback, debug logging
- **`0.3.0` — added Listen Notes fallback provider, new client module, unified metadata structure, expanded multi‑provider architecture**
