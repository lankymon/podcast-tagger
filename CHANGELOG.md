# Changelog

All notable changes to this project will be documented in this file.

This project adheres to **Semantic Versioning** and follows the **Keep a Changelog** format.

---

## [0.3.0] – 2026‑01‑14

### Added

- Introduced **Listen Notes** as a secondary metadata provider.
- Added new `listennotes_client.py` module for API integration.
- Implemented fallback logic in `core.py` to use Listen Notes when TVDB has no series or missing episodes.
- Unified metadata structure across providers for consistent tagging.
- Expanded README with new environment variable (`LISTEN_NOTES_API_KEY`) and updated architecture overview.

### Changed

- Updated `core.py` orchestration to support multi‑provider metadata resolution.
- Improved pipeline resilience when primary metadata sources lack coverage.

### Notes

- This release lays the groundwork for future providers (e.g., BBC Sounds scraping).

---

## [0.2.0] – 2026‑01‑10

### Added

- Dynamic show detection based on folder name.
- Regex‑based suffix stripping for variants such as `(Live)`, `[Remastered]`, `- New Batch`, etc.
- Initial fallback handling for incomplete TVDB coverage.
- Lightweight debug logging.
- Modular orchestration to support future metadata providers.

### Changed

- Improved `detect_show_name` logic for robustness across naming conventions.

---

## [0.1.0] – 2026‑01‑07

### Added

- Initial project structure.
- Basic TVDB integration.
- MP3 tagging pipeline.
- Environment‑driven configuration.
- Initial test suite.
