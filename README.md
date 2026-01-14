# podcast-tagger

## Overview

Podcast Tagger is a metadata enrichment pipeline for podcast MP3 files. It fetches episode data from TheTVDB, matches it to local audio files, and applies ID3 tags including title, episode number, description, and artwork.

Originally designed for SmartLess episodes stored on a local NAS, the system now supports **dynamic detection of any show** based on the folder name. This includes robust **regex‑based stripping of suffixes** such as `(Live)`, `[Remastered]`, and `- New Batch`, ensuring consistent show identification even when folder names vary.

The pipeline also includes:

- fallback handling for incomplete TVDB coverage
- lightweight debug logging
- modular orchestration for future expansion

---

## Setup

To create and activate the virtual environment and install dependencies:

```bash
./setup_env.ps1
```

Ensure your `.env` file contains:

```env
TVDB_API_KEY=your-api-key-here
MP3_FOLDER=your-mp3-directory
```

> **Note:** `MP3_FOLDER` should point to the folder containing the MP3 files.  
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

---

## Notebooks

To launch Jupyter Lab inside the project environment:

```bash
./start_notebook.ps1
```

---

## Project Structure

- `src/podcast_tagger/` – source code modules
  - `core.py` – orchestration logic (show detection, metadata fetch, pipeline coordination)
  - `tvdb_client.py` – TVDB API integration with fallback handling
  - `tagger.py` – MP3 tagging logic
  - `utils.py` – filename and string helpers (including regex‑based show name detection)
  - `config.py` – environment‑driven configuration
- `notebooks/` – exploratory notebooks
- `datasets/` – project‑specific datasets (not synced)
- `metadata/` – serialized JSONs (cached episode metadata)
- `scripts/` – helper scripts (per‑project)
- `main.py` – entry point for the tagging pipeline
- `.env` – environment variables (not committed)
- `requirements.txt` – Python dependencies

---

## Version

This project follows semantic versioning.

- Initial version: `0.1.0`
- Current version: `0.2.0` – dynamic show detection, regex‑based suffix stripping, TVDB fallback, debug logging, and modular orchestration
