---
name: image
description: Generate, edit, or create any image — photos, illustrations, website visuals, placeholders, icons, thumbnails, banners, or any graphic asset
argument-hint: describe what image you want to generate or edit
user_invocable: true
allowed-tools:
  - Bash
  - Read
  - Write
  - AskUserQuestion
---

Generate or edit an image using the Nano Banana script.

User request: $ARGUMENTS

## Task

1. Determine the mode from the request.
2. Craft a descriptive prompt (narrative, not keywords). For detailed templates, read `$CLAUDE_PLUGIN_ROOT/skills/genimage/references/prompting-guide.md`.
3. Run the script with correct flags.
4. Show the result to the user.

```
python "$CLAUDE_PLUGIN_ROOT/scripts/genimage.py" --prompt "..." [options]
```

## Mode → Flags

| Mode | Flags |
|------|-------|
| Text-to-image | `--prompt "..."` only |
| Image editing | `--prompt "edit instructions" --images source.png` |
| Style transfer | `--prompt "Apply style..." --images style.png target.png` |
| Multi-image composition | `--prompt "..." --images a.png b.png [...]` (up to 14) |
| High-resolution | add `--resolution 2K` or `4K` to any mode (triggers Pro model) |

## All Flags

| Flag | Required | Default |
|------|----------|---------|
| `--prompt "text"` | Yes | — |
| `--output file.png` | No | `generated_image.png` |
| `--images path [...]` | No | — |
| `--aspect-ratio RATIO` | No | — |
| `--resolution 1K\|2K\|4K` | No | — |

Aspect ratios: `1:1` `2:3` `3:2` `3:4` `4:3` `4:5` `5:4` `9:16` `16:9` `21:9`

Editing is text-guided — describe what to change and Gemini handles region detection automatically.

If the script fails due to a missing API key, advise the user to run `/nano-banana:setup`.
