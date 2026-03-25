---
name: Gemini Image Generation
description: Knowledge for generating and editing images using the Gemini 3.1 API. Nano Banana 2 (Flash) and Nano Banana Pro (Pro). Use for artwork, style transfer, 4K generation, or any visual content creation.
version: 2.0.0
---

# Gemini Image Generation Skill

Knowledge for the Gemini API image generation suite (Nano Banana 2 and Pro).

## Models

- **Nano Banana 2** (`gemini-3.1-flash-image-preview`): Fast, high-efficiency. Used by default.
- **Nano Banana Pro** (`gemini-3-pro-image-preview`): Professional asset production, advanced reasoning, high-fidelity text, up to 4K. Used automatically when `--resolution` is specified.

## Setup

If the API key is not configured, run `/nano-banana:setup`.

## Script

All image generation is handled by a single script:

```
python "$CLAUDE_PLUGIN_ROOT/scripts/genimage.py" --prompt "..." [options]
```

## Modes

| Mode | Flags |
|------|-------|
| Text-to-image | `--prompt "..."` (no `--images`) |
| Image editing | `--prompt "edit instructions" --images source.png` |
| Style transfer | `--prompt "Apply the style of the first image to the second" --images style.png source.png` |
| Multi-image composition / reference | `--prompt "..." --images a.png b.png [c.png ...]` (up to 14) |
| High-resolution (2K / 4K) | add `--resolution 2K` or `--resolution 4K` to any mode |

## Flags

- `--prompt "text"` — required
- `--output filename.png` — optional
- `--images path [path ...]` — input image(s); omit for pure text-to-image
- `--aspect-ratio` — `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`
- `--resolution 1K|2K|4K` — triggers Pro model

## Resolutions

- `1K` — 1024 px
- `2K` — 2048 px
- `4K` — 4096 px

Must use uppercase K.

## Prompting Template
"A photorealistic [shot type] of [subject], [action], set in [environment]. [Lighting], [mood]. Captured with [camera/lens]. [aspect ratio]."
