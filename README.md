# YouTube MP3 Downloader - Enhanced

![Build and Test](https://github.com/yourusername/ytdownloader/actions/workflows/build.yml/badge.svg)

A powerful and user-friendly Python script to download audio from YouTube videos and playlists as MP3/FLAC/M4A files with quality options, metadata embedding, batch processing, rich error handling, and configuration management.

## ✨ Features

### Core Features
- 🎵 **Multiple Quality Presets**: Low (128k), Medium (192k), High (320k), Best (original)
- 🎼 **Multiple Audio Formats**: MP3, M4A, FLAC, WAV, OGG
- 📋 **Playlist Support**: Download entire playlists with one command
- 📁 **Batch Downloads**: Process multiple URLs from a text file
- 🎨 **Enhanced Progress Display**: Beautiful progress bars with download speed and ETA
- 📝 **Metadata Embedding**: Automatic ID3 tags and album artwork
- 🎯 **Custom Output**: Configurable output directories and filename templates
- 🎨 **Color-Coded Output**: Easy-to-read console messages with status indicators

### Advanced Features
- ⚙️ **Configuration File Support**: Save and load settings from `.ytdownloader.conf`
- 📜 **Archive Tracking**: Never re-download the same video twice
- 📊 **Detailed Logging**: Log all downloads to file for history and debugging
- 🔍 **Dry-Run Mode**: Preview what would be downloaded without actually downloading
- 🌐 **Network Options**: Proxy support, rate limiting, cookie authentication
- ⚡ **Robust Error Handling**: Automatic retries with exponential backoff
- ✅ **Preflight Validation**: Check URLs, FFmpeg, and permissions before downloading
- 📈 **Batch Reporting**: Detailed summary of batch download results

## Requirements

- Python 3.8+
- ffmpeg (for audio conversion)
- yt-dlp
- rich (for beautiful output)

## Installation

### Quick Start

1. **Clone or download the repository**:
```bash
git clone <repository_url>
cd ytdownloader
```

2. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

3. **Install ffmpeg** (if not already installed):
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
# Or use: choco install ffmpeg
```

### Using Makefile (Optional)

```bash
# Install dependencies
make install

# Run the script
make run URL="https://www.youtube.com/watch?v=VIDEO_ID"

# Run tests
make test
```

## Usage

### Basic Usage

Download a single video with default settings (medium quality MP3):
```bash
python youtube_mp3_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Quality Options

```bash
python youtube_mp3_downloader.py -q low <url>      # Low (128 kbps)
python youtube_mp3_downloader.py -q medium <url>   # Medium (192 kbps, default)
python youtube_mp3_downloader.py -q high <url>     # High (320 kbps)
python youtube_mp3_downloader.py -q best <url>     # Best (original)
```

### Audio Format Options

```bash
python youtube_mp3_downloader.py -f mp3 <url>      # MP3 (default)
python youtube_mp3_downloader.py -f m4a <url>      # M4A
python youtube_mp3_downloader.py -f flac <url>     # FLAC (lossless)
python youtube_mp3_downloader.py -f wav <url>      # WAV
python youtube_mp3_downloader.py -f ogg <url>      # OGG
```

### Playlist Downloads

```bash
python youtube_mp3_downloader.py -p <playlist_url>
python youtube_mp3_downloader.py -p -q high -f flac <playlist_url>
```

### Batch Downloads

Create a text file with URLs (one per line):
```
# urls.txt
https://www.youtube.com/watch?v=VIDEO_ID_1
https://www.youtube.com/watch?v=VIDEO_ID_2
https://www.youtube.com/playlist?list=PLAYLIST_ID
```

```bash
python youtube_mp3_downloader.py -b urls.txt
python youtube_mp3_downloader.py -b urls.txt -q best -o ./my_music
python youtube_mp3_downloader.py -b urls.txt --retries 5 --log-file download.log
python youtube_mp3_downloader.py -b urls.txt --fail-fast
python youtube_mp3_downloader.py -b urls.txt --max-failures 3
```

### Dry-Run Mode

Preview what would be downloaded without actually downloading:
```bash
python youtube_mp3_downloader.py --dry-run <url>
python youtube_mp3_downloader.py --dry-run -b urls.txt
```

### Configuration Management

#### Show Current Configuration
```bash
python youtube_mp3_downloader.py --show-config
```

#### Save Settings to Config File
```bash
python youtube_mp3_downloader.py --save-config
```

Creates a config file at `~/.ytdownloader.conf`.

#### Using Config Files

The script looks for config files in this order:
1. `~/.ytdownloader.conf` (home directory)
2. `./.ytdownloader.conf` (current directory)
3. `./ytdownloader.conf` (current directory)

Example `~/.ytdownloader.conf`:
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

### Archive/History

Never download the same video twice:
```bash
python youtube_mp3_downloader.py <url>                           # Archive enabled (default)
python youtube_mp3_downloader.py --no-archive <url>              # Disable archive
python youtube_mp3_downloader.py --archive /path/to/archive <url> # Custom archive
```

### Logging

Log all downloads to a file:
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
python youtube_mp3_downloader.py --limit-rate 500K <url>

# Using cookies
python youtube_mp3_downloader.py --cookies cookies.txt <url>
```

### Custom Output Directory

```bash
python youtube_mp3_downloader.py -o ./my_music <url>
python youtube_mp3_downloader.py --output /path/to/music <url>
```

### Custom Filename Templates

```bash
python youtube_mp3_downloader.py -t "%(artist)s - %(title)s" <url>
python youtube_mp3_downloader.py -t "%(upload_date)s - %(title)s" <url>
python youtube_mp3_downloader.py -t "%(uploader)s - %(title)s" <url>
```

Available variables: `%(title)s`, `%(artist)s`, `%(uploader)s`, `%(upload_date)s`, `%(id)s`, `%(ext)s`

### Error Handling & Retries

```bash
python youtube_mp3_downloader.py <url>                  # Default 3 retries
python youtube_mp3_downloader.py --retries 5 <url>      # Custom retry count
python youtube_mp3_downloader.py --skip-checks <url>    # Skip validation
```

### Other Options

```bash
python youtube_mp3_downloader.py --no-metadata <url>     # No metadata
python youtube_mp3_downloader.py --no-thumbnail <url>    # No thumbnails
python youtube_mp3_downloader.py --quiet <url>           # Quiet mode
python youtube_mp3_downloader.py --version               # Show version
```

## Complete Command-Line Reference

```
usage: youtube_mp3_downloader.py [-h] 
                                  [-q {low,medium,high,best}] 
                                  [-f {mp3,m4a,flac,wav,ogg}]
                                  [-o OUTPUT] [-t TEMPLATE] [-p] [-b BATCH_FILE]
                                  [--no-metadata] [--no-thumbnail]
                                  [--retries RETRIES] [--fail-fast] [--max-failures MAX_FAILURES]
                                  [--skip-checks] [--archive ARCHIVE] [--no-archive]
                                  [--proxy PROXY] [--limit-rate LIMIT_RATE] [--cookies COOKIES]
                                  [--log-file LOG_FILE] [--dry-run] 
                                  [--save-config] [--show-config]
                                  [--quiet] [--version]
                                  [url]
```

### Quality & Format
- `-q, --quality` - Audio quality: low, medium, high, best (default: medium)
- `-f, --format` - Audio format: mp3, m4a, flac, wav, ogg (default: mp3)

### Output Options
- `-o, --output` - Output directory (default: ./downloads)
- `-t, --template` - Filename template (default: %(title)s.%(ext)s)

### Download Options
- `-p, --playlist` - Download entire playlist
- `-b, --batch-file` - Download from batch file (one URL per line)
- `--no-metadata` - Do not embed metadata
- `--no-thumbnail` - Do not embed thumbnail as album art

### Error Handling
- `--retries` - Max retry attempts for network errors (default: 3)
- `--fail-fast` - Stop batch processing on first failure
- `--max-failures` - Stop batch after N failures (0 = no limit)
- `--skip-checks` - Skip preflight validation checks

### Archive & History
- `--archive` - Archive file path (default: ~/.ytdownloader_archive.txt)
- `--no-archive` - Disable archive (re-download already downloaded videos)

### Network
- `--proxy` - Proxy URL (e.g., socks5://127.0.0.1:1080)
- `--limit-rate` - Download rate limit (e.g., 1M, 500K)
- `--cookies` - Path to cookies file for authentication

### Logging & Dry-Run
- `--log-file` - Log file path for detailed logging
- `--dry-run` - Preview what would be downloaded without downloading

### Configuration
- `--save-config` - Save current settings to config file
- `--show-config` - Show current configuration and exit

### Other
- `--quiet` - Suppress output messages
- `--version` - Show program version and exit
- `-h, --help` - Show help message and exit

## Exit Codes

- `0` - All downloads successful
- `1` - Some downloads failed (partial success)
- `2` - Validation/preflight error
- `3` - All downloads failed

## Quality Guide

| Preset | Bitrate | File Size | Use Case |
|--------|---------|-----------|----------|
| low    | 128 kbps | ~1 MB/min | Audiobooks, podcasts, saving space |
| medium | 192 kbps | ~1.5 MB/min | General music listening (default) |
| high   | 320 kbps | ~2.5 MB/min | High-quality music |
| best   | Original | Varies | Archival, best possible quality |

## Format Guide

| Format | Type | Quality | Compatibility |
|--------|------|---------|---|
| MP3    | Lossy | Good | Universal - all devices |
| M4A    | Lossy | Better | Apple devices |
| FLAC   | Lossless | Perfect | Audiophiles |
| WAV    | Lossless | Perfect | Audio editing |
| OGG    | Lossy | Good | Open source |

## Troubleshooting

**Error: No module named 'yt_dlp'**
```bash
pip install -r requirements.txt
```

**Error: FFmpeg not found**
- Install ffmpeg using the installation instructions above
- Verify: `ffmpeg -version`

**Error: Permission denied**
- Make sure you have write permissions to the output directory
- Try a different output directory: `python youtube_mp3_downloader.py -o ~/downloads <url>`

**Downloads are slow**
- This is normal for high-quality files
- Try a lower quality: `-q low` or `-q medium`

**Playlist not downloading**
- Make sure to use the `-p` flag for playlists
- Verify the playlist URL is correct and public

**Some videos fail in batch**
- Check logs: `--log-file debug.log`
- Increase retries: `--retries 5`

**Video marked as "already downloaded"**
- Use `--no-archive` to force re-download
- Or: `rm ~/.ytdownloader_archive.txt`

## Files and Directories

- `youtube_mp3_downloader.py` - Main script
- `requirements.txt` - Python dependencies
- `pyproject.toml` - Project configuration
- `Makefile` - Build automation
- `tests/` - Test suite
- `downloads/` - Default output directory
- `~/.ytdownloader.conf` - User configuration
- `~/.ytdownloader_archive.txt` - Download history

## Notes

- Files are saved in the `downloads` folder by default
- Metadata includes title, artist, and album art
- Progress bars show speed, percentage, and ETA
- Batch processing continues even if some downloads fail
- All paths are created automatically
- Archive prevents downloading the same video twice
- Configuration files make it easy to save settings

## Testing

Run the test suite:
```bash
make test
# or
python -m pytest tests/ -v
```

## License

Free to use and modify for personal and educational purposes.
