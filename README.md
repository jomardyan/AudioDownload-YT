# YouTube MP3 Downloader

![Build and Test](https://github.com/jomardyan/ytdownloader/actions/workflows/build.yml/badge.svg)
![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

A robust, production-grade Python utility for downloading and converting audio from YouTube videos, playlists, and batch sources into multiple audio formats with advanced quality control, metadata management, and comprehensive error handling.

## Features

**Core Capabilities**
- Multiple audio quality presets (128 kbps, 192 kbps, 320 kbps, original)
- Support for multiple formats: MP3, M4A, FLAC, WAV, OGG
- Playlist download support with automatic metadata extraction
- Batch processing with configurable failure handling
- Comprehensive progress reporting with real-time metrics

**Advanced Functionality**
- Persistent download archive to prevent duplicate processing
- Flexible configuration file system with multiple location support
- Detailed logging and error classification
- Dry-run mode for previewing downloads without processing
- Network optimization: proxy support, rate limiting, cookie authentication
- Automatic retry logic with exponential backoff
- Pre-execution validation of dependencies and permissions
- Customizable output directories and filename templates

## System Requirements

- **Python**: 3.8 or higher
- **FFmpeg**: For audio format conversion
- **Dependencies**: yt-dlp, rich (specified in requirements.txt)

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/jomardyan/ytdownloader.git
cd ytdownloader
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) or use:
```bash
choco install ffmpeg
```

### 4. Verify Installation

```bash
python youtube_mp3_downloader.py --version
```

## Quick Start

### Download Single Video

```bash
python youtube_mp3_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Download with Specific Quality and Format

```bash
python youtube_mp3_downloader.py -q high -f flac "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Download Entire Playlist

```bash
python youtube_mp3_downloader.py -p "https://www.youtube.com/playlist?list=PLAYLIST_ID"
```

### Batch Download from File

```bash
python youtube_mp3_downloader.py -b urls.txt
```

## Usage

### Audio Quality Options

| Preset | Bitrate | Typical Use Case |
|--------|---------|------------------|
| `low` | 128 kbps | Audiobooks, podcasts |
| `medium` | 192 kbps | General listening (default) |
| `high` | 320 kbps | High-quality music |
| `best` | Original | Archival, maximum quality |

```bash
python youtube_mp3_downloader.py -q high <url>
```

### Supported Audio Formats

```bash
python youtube_mp3_downloader.py -f mp3 <url>    # MP3 (default)
python youtube_mp3_downloader.py -f m4a <url>    # M4A
python youtube_mp3_downloader.py -f flac <url>   # FLAC (lossless)
python youtube_mp3_downloader.py -f wav <url>    # WAV (lossless)
python youtube_mp3_downloader.py -f ogg <url>    # OGG Vorbis
```

### Playlist Processing

```bash
# Download entire playlist
python youtube_mp3_downloader.py -p <playlist_url>

# Download playlist with specific quality
python youtube_mp3_downloader.py -p -q high -f flac <playlist_url>
```

### Batch Processing

Create a text file with URLs (one per line):

```
https://www.youtube.com/watch?v=VIDEO_ID_1
https://www.youtube.com/watch?v=VIDEO_ID_2
https://www.youtube.com/playlist?list=PLAYLIST_ID
```

```bash
# Standard batch download
python youtube_mp3_downloader.py -b urls.txt

# With quality and output directory
python youtube_mp3_downloader.py -b urls.txt -q best -o ./music

# With retry and logging
python youtube_mp3_downloader.py -b urls.txt --retries 5 --log-file download.log

# Stop on first failure
python youtube_mp3_downloader.py -b urls.txt --fail-fast

# Stop after N failures
python youtube_mp3_downloader.py -b urls.txt --max-failures 3
```

### Output and Naming

```bash
# Custom output directory
python youtube_mp3_downloader.py -o ~/Music <url>

# Custom filename template
python youtube_mp3_downloader.py -t "%(artist)s - %(title)s" <url>
python youtube_mp3_downloader.py -t "%(uploader)s - %(upload_date)s - %(title)s" <url>
```

Available variables: `%(title)s`, `%(artist)s`, `%(uploader)s`, `%(upload_date)s`, `%(id)s`, `%(ext)s`

### Dry-Run Mode

Preview downloads without processing:

```bash
python youtube_mp3_downloader.py --dry-run <url>
python youtube_mp3_downloader.py --dry-run -b urls.txt
```

### Configuration Management

```bash
# Display current configuration
python youtube_mp3_downloader.py --show-config

# Save configuration to file
python youtube_mp3_downloader.py --save-config
```

Configuration files are stored at (in priority order):
1. `~/.ytdownloader.conf` (home directory)
2. `./.ytdownloader.conf` (current directory)
3. `./ytdownloader.conf` (current directory)

**Configuration File Example:**
```ini
[download]
quality=high
format=flac
output=/home/user/Music
template=%(artist)s - %(title)s
embed_metadata=true
embed_thumbnail=true
retries=3

[archive]
use_archive=true
archive_file=~/.ytdownloader_archive.txt

[network]
proxy=
rate_limit=1M
cookies_file=

[logging]
log_file=/home/user/.ytdownloader.log
```

### Download History

Prevent re-downloading the same content:

```bash
# Use archive (default, enabled)
python youtube_mp3_downloader.py <url>

# Disable archive
python youtube_mp3_downloader.py --no-archive <url>

# Use custom archive file
python youtube_mp3_downloader.py --archive /path/to/archive <url>
```

### Logging

Enable detailed logging for debugging:

```bash
python youtube_mp3_downloader.py -b urls.txt --log-file download.log
```

### Network Options

```bash
# HTTP proxy
python youtube_mp3_downloader.py --proxy http://user:pass@host:port <url>

# SOCKS5 proxy
python youtube_mp3_downloader.py --proxy socks5://127.0.0.1:1080 <url>

# Rate limiting
python youtube_mp3_downloader.py --limit-rate 1M <url>

# Cookie authentication
python youtube_mp3_downloader.py --cookies cookies.txt <url>
```

### Error Handling

```bash
# Custom retry attempts
python youtube_mp3_downloader.py --retries 5 <url>

# Skip validation checks
python youtube_mp3_downloader.py --skip-checks <url>

# Disable metadata and thumbnails
python youtube_mp3_downloader.py --no-metadata --no-thumbnail <url>
```

## Command Reference

```
usage: youtube_mp3_downloader.py [-h] [-q {low,medium,high,best}] 
                                  [-f {mp3,m4a,flac,wav,ogg}]
                                  [-o OUTPUT] [-t TEMPLATE] [-p] [-b BATCH_FILE]
                                  [--no-metadata] [--no-thumbnail]
                                  [--retries RETRIES] [--fail-fast] 
                                  [--max-failures MAX_FAILURES]
                                  [--skip-checks] [--archive ARCHIVE] 
                                  [--no-archive]
                                  [--proxy PROXY] [--limit-rate LIMIT_RATE] 
                                  [--cookies COOKIES]
                                  [--log-file LOG_FILE] [--dry-run] 
                                  [--save-config] [--show-config]
                                  [--quiet] [--version] [url]
```

### Download Options
- `-q, --quality {low,medium,high,best}` — Audio quality preset (default: medium)
- `-f, --format {mp3,m4a,flac,wav,ogg}` — Output format (default: mp3)
- `-o, --output OUTPUT` — Output directory (default: ./downloads)
- `-t, --template TEMPLATE` — Filename template (default: %(title)s.%(ext)s)
- `-p, --playlist` — Download entire playlist
- `-b, --batch-file BATCH_FILE` — Process URLs from file

### Processing Options
- `--no-metadata` — Skip metadata embedding
- `--no-thumbnail` — Skip thumbnail artwork embedding
- `--dry-run` — Preview without downloading
- `--quiet` — Suppress console output

### Error Handling
- `--retries RETRIES` — Maximum retry attempts (default: 3)
- `--fail-fast` — Stop batch on first failure
- `--max-failures MAX_FAILURES` — Stop batch after N failures (0 = unlimited)
- `--skip-checks` — Skip preflight validation

### Archive Options
- `--archive ARCHIVE` — Custom archive file location
- `--no-archive` — Disable download history

### Network Options
- `--proxy PROXY` — Proxy URL (e.g., socks5://127.0.0.1:1080)
- `--limit-rate LIMIT_RATE` — Rate limit (e.g., 1M, 500K)
- `--cookies COOKIES` — Path to cookies file

### Configuration & Logging
- `--log-file LOG_FILE` — Log file path
- `--save-config` — Save configuration to file
- `--show-config` — Display current configuration

### Information
- `--version` — Show version information
- `-h, --help` — Show help message

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All downloads completed successfully |
| 1 | Some downloads failed (partial success) |
| 2 | Validation or preflight error |
| 3 | All downloads failed |

## Troubleshooting

### "No module named 'yt_dlp'"
Install dependencies:
```bash
pip install -r requirements.txt
```

### "FFmpeg not found"
Install FFmpeg using the platform-specific instructions in the Installation section.
Verify: `ffmpeg -version`

### "Permission denied"
Ensure write permissions to output directory:
```bash
python youtube_mp3_downloader.py -o ~/Downloads <url>
```

### Downloads are slow
- High-quality downloads are expected to be slower
- Try a lower quality: `-q low` or `-q medium`
- Check network connection and rate limits

### Playlist download fails
- Verify playlist URL is correct and publicly accessible
- Use `-p` flag for playlist URLs
- Check playlist contains available videos

### Some batch downloads fail
Check log file for error details:
```bash
python youtube_mp3_downloader.py -b urls.txt --log-file debug.log
```

Increase retry attempts:
```bash
python youtube_mp3_downloader.py -b urls.txt --retries 5
```

### Video marked as "already downloaded"
Force re-download:
```bash
python youtube_mp3_downloader.py --no-archive <url>
```

Or clear archive:
```bash
rm ~/.ytdownloader_archive.txt
```

## Project Structure

```
youtube_mp3_downloader/
├── youtube_mp3_downloader.py  # Main application
├── requirements.txt            # Python dependencies
├── pyproject.toml             # Project metadata
├── Makefile                   # Build automation
├── .gitignore                 # Git ignore rules
├── .github/
│   └── workflows/
│       └── build.yml          # CI/CD pipeline
├── tests/
│   └── test_smoke.py          # Test suite
└── downloads/                 # Default output directory
```

## Development

### Run Tests

```bash
# Using Makefile
make test

# Using pytest directly
python -m pytest tests/ -v

# With coverage reporting
python -m pytest tests/ -v --cov=. --cov-report=html
```

### Build and Install Locally

```bash
# Install in development mode
pip install -e .

# Install with dev dependencies
pip install -e ".[dev]"
```

## License

This project is licensed under the MIT License — see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## Acknowledgments

This project uses:
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — YouTube extraction and download
- [rich](https://github.com/Textualize/rich) — Rich terminal output
- [FFmpeg](https://ffmpeg.org/) — Audio processing and conversion
