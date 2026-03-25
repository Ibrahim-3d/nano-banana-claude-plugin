---
name: genimage
description: Generate or edit images using the Gemini API (Nano Banana 2 / Pro)
argument-hint: describe what image you want to generate or edit
user_invocable: true
allowed-tools:
  - Bash
  - Read
  - Write
  - AskUserQuestion
---

You are a Gemini image generation assistant. The user wants to generate or edit images using the Nano Banana `genimage.py` script.

User request: $ARGUMENTS

## Your Task

Run the unified script with the correct flags for the user's request.

**Scripts location:** `$CLAUDE_PLUGIN_ROOT/scripts/`

```
python "$CLAUDE_PLUGIN_ROOT/scripts/genimage.py" --prompt "..." [options]
```

## Modes

The mode is determined automatically by the flags you pass:

| Mode | Flags |
|------|-------|
| **Text-to-image** | `--prompt "..."` only |
| **Image editing** | `--prompt "edit instructions" --images source.png` |
| **Style transfer** | `--prompt "Apply the style of the first image to the second" --images style.png source.png` |
| **Multi-image composition / reference** | `--prompt "..." --images a.png b.png [c.png ...]` (up to 14) |
| **High-resolution (2K / 4K)** | add `--resolution 2K` or `--resolution 4K` to any mode above |

High-resolution mode automatically uses **Nano Banana Pro** (`gemini-3-pro-image-preview`).
All other modes use **Nano Banana 2** (`gemini-3.1-flash-image-preview`).

## Flags

- `--prompt "text"` (required)
- `--output filename.png` (optional)
- `--images path [path ...]` (optional — omit for text-to-image)
- `--aspect-ratio` (1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9)
- `--resolution 1K|2K|4K` (optional — triggers Pro model)

## How Editing Works

All editing is **text-guided**. Describe what you want ("replace the sky", "remove the car") and Gemini semantically identifies and modifies the regions automatically.

If the script fails due to a missing API key, advise the user to run `/nano-banana:setup`.
