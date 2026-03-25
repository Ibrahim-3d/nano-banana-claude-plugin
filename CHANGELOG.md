# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [2.0.0] - 2026-03-25

### Changed
- Consolidated eight specialized generation scripts (`texttoimage.py`, `imageedit.py`,
  `hires.py`, `compose.py`, `multiref.py`, `styletransfer.py`, `searchground.py`,
  `multiturn.py`) into a single universal `scripts/genimage.py`.
- Model selection is now automatic: `--resolution` triggers Nano Banana Pro; everything
  else uses Nano Banana 2.
- Style transfer is now expressed via `--images style.png source.png` plus a descriptive
  prompt, eliminating the `--style-image` flag.

### Removed
- `scripts/searchground.py` — Google Search grounding is redundant when the plugin is
  called by a language model that already has search capability.
- `scripts/multiturn.py` — multi-turn conversation is managed by Claude, not the script;
  the old implementation was stateless and misleading.
- All now-merged scripts: `texttoimage.py`, `imageedit.py`, `hires.py`, `compose.py`,
  `multiref.py`, `styletransfer.py`.

## [1.3.0] - 2026-03-19

### Added
- Upgraded all scripts to use **Gemini 3.1** models (**Nano Banana 2** and **Nano Banana Pro**)
- Added `/nano-banana:setup` command to easily configure the Gemini API key
- Added `scripts/utils.py` for centralized client and model management
- Added `scripts/setup_key.py` to handle API key persistence
- Improved `check_env.py` to suggest the setup command on key failure

### Changed
- Moved default model from `gemini-2.5-flash-image` to `gemini-3.1-flash-image-preview`
- Updated documentation and skill knowledge to reflect Gemini 3.1 capabilities (grounding, chat, 14-image multiref)

## [1.2.0] - 2026-03-19

### Added
- Standardized plugin structure for Claude Code
- Added `marketplace.json` for Ibrahim-3d marketplace integration
- Added `settings.json` to auto-activate the Gemini Image Generation agent
- Added `SessionStart` hook with `check_env.py` to verify Gemini API key configuration
- Added `icon` metadata to `plugin.json`

### Changed
- Refined `plugin.json` by removing redundant directory paths (relying on Claude Code defaults)
- Updated author information to include full name and URL

## [1.1.0] - 2026-02-11
...
