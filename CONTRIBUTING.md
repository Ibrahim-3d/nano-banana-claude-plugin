# Contributing to Nano Banana

Thanks for your interest in contributing to the Nano Banana plugin! Contributions of all kinds are welcome — bug fixes, new generation modes, documentation improvements, and more.

## How to Contribute

1. **Fork** the repository on GitHub
2. **Clone** your fork: `git clone https://github.com/<your-username>/nano-banana-claude-plugin.git`
3. **Create a feature branch**: `git checkout -b feature/new-mode`
4. **Make your changes** (see conventions below)
5. **Test locally** with `claude --plugin-dir /path/to/your/fork`
6. **Commit** your changes with a clear message
7. **Push** to your fork: `git push origin feature/new-mode`
8. **Open a Pull Request** against `main` and describe what you changed and why

## Adding a New Generation Mode

1. Extend `scripts/genimage.py` with the new flags or behavior
2. Update `commands/genimage.md` with the new mode
3. Update the agent at `agents/gemini-image-gen.md`
4. Update the skill at `skills/genimage/SKILL.md`
5. Update `README.md` with the new mode
6. Update `CHANGELOG.md`

## Script Conventions

- Use `argparse` with `--prompt` as required argument
- Load `.env` via `SCRIPT_DIR` pattern (not hardcoded paths)
- Support `--output`, `--aspect-ratio`, and `--image`/`--images` flags where applicable
- Print the output filename on success
- Handle missing API key errors gracefully and suggest running `/nano-banana:setup`

## Reporting Issues

Open an issue on GitHub with:
- What you expected to happen
- What actually happened
- Steps to reproduce
- Your Python version, OS, and plugin version (`plugin.json`)

## Code of Conduct

Be respectful and constructive. This is a welcoming project for contributors of all experience levels.
