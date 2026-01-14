# podcast-tagger

## Overview

Podcast Tagger is a metadata enrichment pipeline for podcast MP3 files. It fetches episode data from TheTVDB, matches it to local audio files, and applies ID3 tags including title, episode number, description, and artwork. The system is designed for automated tagging of SmartLess episodes stored on a local NAS, but the structure supports extension to other shows.

## Setup

To create and activate the virtual environment and install dependencies:

```
.\setup_env.ps1
```

Ensure your `.env` file contains:

```
TVDB_API_KEY=your-api-key-here
SMARTLESS_MP3_FOLDER=your-mp3-directory
```

## Running Tests

To run the test suite:

```
.\run_tests.ps1
```

## Notebooks

To launch Jupyter Lab inside the project environment:

```
.\start_notebook.ps1
```

## Project Structure

- `src/podcast_tagger/` — source code modules
  - `core.py` — orchestration logic
  - `tvdb_client.py` — API integration
  - `tagger.py` — MP3 tagging logic
  - `utils.py` — filename and string helpers
  - `config.py` — environment-driven configuration
- `tests/` — test suite
- `notebooks/` — exploratory notebooks
- `data/` — project-specific datasets (not synced)
  - `external/smartless.json` — cached episode metadata
- `scripts/` — helper scripts (per-project)
- `main.py` — entry point for the tagging pipeline
- `.env` — environment variables
- `requirements.txt` — Python dependencies

## Version

This project follows semantic versioning.  
Initial version: `0.1.0`

---
