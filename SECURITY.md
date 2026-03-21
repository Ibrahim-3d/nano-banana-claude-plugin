# Security Policy

## API Key Safety

This plugin requires a Google Gemini API key stored in `scripts/.env`. This file is excluded from version control via `.gitignore`.

**Never commit your `.env` file.** If you accidentally expose your API key, rotate it immediately at [Google AI Studio](https://aistudio.google.com/apikey).

## Reporting a Vulnerability

If you discover a security vulnerability, please open a private issue on GitHub or contact the maintainer directly.

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.3.x   | ✅ Yes    |
| 1.2.x   | ✅ Yes    |
| 1.1.x   | ⚠️ Best-effort |
| < 1.1   | ❌ No     |
