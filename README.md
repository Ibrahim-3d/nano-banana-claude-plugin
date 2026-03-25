<div align="center">

<img src="assets/logo.png" alt="Nano Banana Logo" width="180" />

# Nano Banana 2

**Google Gemini 3.1 AI image generation plugin for Claude Code**

[![Claude Code Plugin](https://img.shields.io/badge/Claude_Code-Plugin-blue?style=flat-square)](https://claude.ai/claude-code)
[![Gemini API](https://img.shields.io/badge/Powered_by-Gemini_3.1-4285F4?style=flat-square&logo=google)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.3.0-orange?style=flat-square)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

*One command. The full power of Gemini 3.1.*

[Features](#features) · [Installation](#installation) · [Quick Start](#quick-start) · [Usage Examples](#usage-examples) · [Models](#models) · [Contributing](#contributing)

</div>

---

<img src="assets/banner.png" alt="Nano Banana — AI image generation for Claude Code" width="100%" />

---

## What is Nano Banana 2?

**Nano Banana 2** brings Google Gemini 3.1's state-of-the-art image generation and editing capabilities directly into [Claude Code](https://claude.ai/claude-code). It ships a smart `/genimage` slash command, an autonomous Gemini image agent, and a single universal Python script covering every generation and editing workflow — all wired together so you never leave your coding environment.

> **Just type `/genimage` and describe what you want.** The agent picks the right script, enhances your prompt, and runs the generation automatically.

```
/genimage a photorealistic cyberpunk street in Cairo, neon palm trees, 16:9
```

---

## Features

### 🖼️ Image Generation
| Feature | Description |
|---------|-------------|
| **Text-to-Image** | Generate any image from a text prompt (Gemini 3.1 Flash) |
| **High-Resolution (2K / 4K)** | Professional-grade assets up to 4K (Gemini 3 Pro) |
| **Search-Grounded Generation** | Images informed by real-time Google Search data |
| **14-Image Multi-Reference** | Mix up to 14 reference images for consistent characters & objects |

### ✏️ AI-Powered Image Editing (Text-Guided, No Masks)
| Feature | Description |
|---------|-------------|
| **Inpainting** | "Replace the sky with a sunset" — no mask required |
| **Object Manipulation** | "Remove the car" or "Add a cat on the sofa" |
| **Style Transfer** | Apply the artistic style of one image to another |
| **Multi-Image Composition** | Blend elements from multiple source images |
| **Multi-Turn Chat Editing** | Iteratively refine images through conversation |

### ⚡ Developer Experience
- **Zero context-switching** — generate images without leaving Claude Code
- **Autonomous agent** — auto-selects the best script for your request
- **Smart prompt enhancement** — the agent crafts effective prompts for you
- **All aspect ratios** — 1:1, 16:9, 9:16, 4:3, 3:4, 21:9, and more

---

## Installation

### Option 1: Marketplace (Recommended)

```bash
/plugin marketplace add Ibrahim-3d/nano-banana-claude-plugin
/plugin install nano-banana@nano-banana-marketplace
```

### Option 2: Direct Install

```bash
/plugin install Ibrahim-3d/nano-banana-claude-plugin
```

### Option 3: Manual Clone

```bash
git clone https://github.com/Ibrahim-3d/nano-banana-claude-plugin.git ~/.claude/plugins/nano-banana
pip install google-genai python-dotenv Pillow
```

---

## Quick Start

**1. Get a free Gemini API key** at [Google AI Studio](https://aistudio.google.com/apikey).

**2. Run the setup command** inside Claude Code:

```bash
/nano-banana:setup
```

**3. Generate your first image:**

```bash
/genimage a golden retriever puppy playing in autumn leaves, soft bokeh, 4:3
```

That's it — Nano Banana handles the rest.

---

## Usage Examples

### Text-to-Image

```bash
/genimage a minimalist flat-design illustration of a coffee shop, pastel colors
/genimage product shot of a black ceramic mug on a marble surface, studio lighting, 1:1
/genimage aerial view of a sci-fi megacity at night, neon lights, cinematic, 21:9
```

### High-Resolution (2K / 4K)

```bash
/genimage a hyper-detailed fantasy castle on a cliff, waterfall, 4K, 16:9
```

### Search-Grounded Generation

```bash
/genimage current Tokyo skyline in cherry blossom season, photorealistic
```

### Image Editing

```bash
# Replace the background of an existing image
/genimage replace the plain background in photo.png with a bustling Tokyo street at night

# Remove an object
/genimage remove the power lines from landscape.png, preserve everything else

# Apply a style
/genimage apply the brushstroke style of starry-night.png to my-photo.jpg
```

### Multi-Turn Iterative Editing

Use image editing with follow-up calls, passing the previously generated image back as input:

```bash
# Step 1 — generate a base image
/genimage a cozy cafe interior, warm lighting, 4:3

# Step 2 — refine the previous output
/genimage add a cat sleeping on the counter --images generated_image.png
```

---

## Models

| Model | Codename | Best For |
|-------|----------|----------|
| `gemini-3.1-flash-image-preview` | **Nano Banana 2** 🍌 | Fast generation, search grounding, 14-ref composition, chat editing |
| `gemini-3-pro-image-preview` | **Nano Banana Pro** ✨ | 2K/4K resolution, professional assets, thinking mode |

---

## Script Reference

All image generation is handled by a **single universal script**:

```
python "$CLAUDE_PLUGIN_ROOT/scripts/genimage.py" --prompt "..." [options]
```

| Mode | How to invoke |
|------|--------------|
| **Text-to-image** | `--prompt "..."` (no `--images`) |
| **Image editing** | `--prompt "edit instructions" --images source.png` |
| **Style transfer** | `--prompt "Apply the style of the first image to the second" --images style.png source.png` |
| **Multi-image composition / reference** | `--prompt "..." --images a.png b.png [c.png ...]` (up to 14) |
| **High-resolution (2K / 4K)** | add `--resolution 2K` or `--resolution 4K` to any mode above |

High-resolution mode automatically uses **Nano Banana Pro**. All other modes use **Nano Banana 2**.

### Flags

| Flag | Description |
|------|-------------|
| `--prompt "text"` | Required — generation or editing instructions |
| `--output filename.png` | Output filename (default: `generated_image.png`) |
| `--images path [path ...]` | Input image(s) — omit for pure text-to-image |
| `--aspect-ratio` | `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `21:9`, and more |
| `--resolution 1K\|2K\|4K` | High-res output (triggers Pro model) |

---

## Requirements

- **Claude Code** (latest)
- **Python 3.9+**
- **Gemini API key** — [Get one free](https://aistudio.google.com/apikey)
- Python packages: `google-genai`, `python-dotenv`, `Pillow`

---

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to:

- Report bugs or request features
- Add a new generation mode
- Follow script conventions

---

## Security

API keys are stored locally in `scripts/.env` and are excluded from version control. See [SECURITY.md](SECURITY.md) for the full security policy.

---

## License

Released under the [MIT License](LICENSE). Free to use, modify, and distribute.

---

<div align="center">

**Built for [Claude Code](https://claude.ai/claude-code)** · Powered by **[Google Gemini 3.1](https://ai.google.dev/)**

**Nano Banana 2** 🍌 · **Nano Banana Pro** ✨ · Made with ❤️ by [Ibrahim-3d](https://github.com/Ibrahim-3d)

*AI image generation · Text-to-image · Image editing · Style transfer · Inpainting · 4K generation · Claude Code plugin*

</div>
