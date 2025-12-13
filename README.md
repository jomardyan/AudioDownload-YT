# AudioDownload-YT

<div align="center">

![Build and Test](https://github.com/jomardyan/AudioDownload-YT/actions/workflows/build.yml/badge.svg)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**A professional, multi-platform media downloader supporting 9+ platforms with advanced quality control and metadata management.**

[Features](#features) • [Installation](#installation) • [Quick Start](#quick-start) • [Documentation](#usage) • [Contributing](#contributing)

</div>

---

## Overview

AudioDownload-YT is a robust, production-grade Python utility for downloading and converting media from multiple platforms into various audio and video formats. Built with a modular plugin architecture, it supports YouTube, TikTok, Instagram, SoundCloud, Spotify, and more, offering advanced quality control, batch processing, and comprehensive error handling.

## Features

### 🎯 Core Capabilities
- **Multiple Quality Presets**: 128 kbps, 192 kbps, 320 kbps, or original quality
- **Format Support**: MP3, M4A, FLAC, WAV, OGG with FFmpeg-powered conversion
- **Playlist Processing**: Automatic extraction and batch download with metadata
- **Batch Operations**: Process multiple URLs from files with configurable failure handling
- **Real-time Progress**: Rich terminal output with live progress tracking and metrics

### 🔌 Multi-Platform Plugin System
Download from **9+ popular platforms** with a unified interface:

| Platform | Status | Playlist | Auth |
|----------|--------|----------|------|
| YouTube | ✅ | ✅ | Optional |
| TikTok | ✅ | ✅ | ❌ |
| Instagram | ✅ | ❌ | ❌ |
| SoundCloud | ✅ | ✅ | ❌ |
| Spotify | ✅ | ✅ | ❌ |
| Twitch | ✅ | ❌ | ❌ |
| Dailymotion | ✅ | ✅ | ❌ |
| Vimeo | ✅ | ✅ | ❌ |
| Reddit | ✅ | ❌ | ❌ |

**Plugin Features:**
- Extensible architecture for adding new platforms
- Automatic platform detection from URL
- Per-platform capability management
- Unified error handling and retry logic

### ⚙️ Advanced Functionality
- **Download Archive**: Persistent history to prevent duplicate downloads
- **Configuration System**: Flexible INI-based configuration with multiple location support
- **Error Handling**: Comprehensive error classification with automatic retry and exponential backoff
- **Dry-run Mode**: Preview downloads without processing
- **Network Features**: Proxy support, rate limiting, cookie authentication
- **Metadata Management**: Automatic embedding of thumbnails and ID3 tags
- **Customization**: Configurable output directories and filename templates
- **Validation**: Pre-execution checks for dependencies and permissions

## System Requirements

| Component | Requirement |
|-----------|-------------|
| **Python** | 3.8 or higher |
| **FFmpeg** | Latest stable version |
| **Dependencies** | yt-dlp, rich (see requirements.txt) |
| **OS Support** | Windows, macOS, Linux |

---

## Installation

### Prerequisites

Ensure you have Python 3.8+ and FFmpeg installed on your system.

### Method 1: Quick Install (Recommended)

```bash
# Clone the repository
git clone https://github.com/jomardyan/AudioDownload-YT.git
cd AudioDownload-YT

# Install with make (installs dependencies automatically)
make install
```

### Method 2: Manual Installation

#### 1. Clone Repository

```bash
git clone https://github.com/jomardyan/AudioDownload-YT.git
cd AudioDownload-YT
```

#### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

#### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Install FFmpeg

<details>
<summary><b>Windows</b></summary>

**Option 1: Using Windows Package Manager (winget) — Recommended**
```powershell
winget install Gyan.FFmpeg
```

**Option 2: Using Chocolatey**
```powershell
choco install ffmpeg
```

**Option 3: Manual Installation**
1. Download from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract to `C:\ffmpeg`
3. Add `C:\ffmpeg\bin` to system PATH

⚠️ **Important**: Restart your terminal after installation for PATH changes to take effect.
</details>

<details>
<summary><b>macOS</b></summary>

```bash
brew install ffmpeg
```
</details>

<details>
<summary><b>Linux (Ubuntu/Debian)</b></summary>

```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**For other distributions:**
- Fedora: `sudo dnf install ffmpeg`
- Arch: `sudo pacman -S ffmpeg`
</details>

### Method 3: Global Installation with pipx

For system-wide access:

```bash
make pipx-install
```

This allows you to run `ytdownloader` from anywhere without activating a virtual environment.

### Verify Installation

```bash
# Check Python installation
python --version

# Check FFmpeg installation
ffmpeg -version

# Verify downloader
python downloader.py --version

# Test basic functionality
python downloader.py --help
```

---

## Quick Start

### Option 1: GUI (Graphical Interface)

For the easiest experience, use the desktop GUI:

```bash
# Launch the GUI
python ytdownloader_gui.py

# Or use Make
make gui
```

The GUI provides a visual interface with dropdowns, progress bars, and real-time logging. Perfect for users who prefer point-and-click over command-line.

### Option 2: Command Line

#### Download Single Video

```bash
python downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

#### Download with Specific Quality and Format

```bash
python downloader.py -q high -f flac "https://www.youtube.com/watch?v=VIDEO_ID"
```

#### Download Entire Playlist

```bash
python downloader.py -p "https://www.youtube.com/playlist?list=PLAYLIST_ID"
```

#### Batch Download from File

```bash
python downloader.py -b urls.txt
```

## 🖥️ GUI (Desktop Application)

A feature-rich Tkinter GUI provides a user-friendly desktop interface for all downloader functionality.

### Features

**🎨 User Interface**
- Clean, intuitive design with tabbed layout
- Multi-line URL input with syntax highlighting
- Real-time progress bars and status indicators
- Rich logging with color-coded messages
- Context menus with cut/copy/paste support
- Keyboard shortcuts for common operations

**⚙️ Configuration Options**
- Quality presets (low, medium, high, best)
- Format selection (MP3, M4A, FLAC, WAV, OGG)
- Custom output directory with file browser
- Playlist support toggle
- Metadata and thumbnail embedding options
- Configurable concurrent downloads (1-5)
- Retry attempts configuration (0-20)
- Download archive management
- Custom filename templates

**🔄 Download Management**
- Batch processing from text files
- Real-time progress tracking per download
- Playlist progress with item counts
- Cancel/pause functionality
- Skip existing files option
- Success/failure statistics
- Detailed error reporting

**📋 Additional Features**
- Save/load URL lists from files
- Export log to text file
- About dialog with version info
- Menu bar with File/Edit/Help menus
- Platform-agnostic design (Windows, macOS, Linux)

### Launch GUI

<details>
<summary><b>From Source</b></summary>

```bash
# Direct execution
python ytdownloader_gui.py

# Using Make
make gui
```
</details>

<details>
<summary><b>After Package Installation</b></summary>

```bash
# Using the GUI command
ytdownloader-gui

# Alternative alias
ytdl-gui
```
</details>

<details>
<summary><b>With Virtual Environment</b></summary>

```bash
# Windows
.venv\Scripts\activate
python ytdownloader_gui.py

# macOS/Linux
source .venv/bin/activate
python ytdownloader_gui.py
```
</details>

### GUI Workflow

1. **Enter URLs**: Paste one or more URLs (one per line) in the text box
2. **Configure Options**: Select quality, format, and output directory
3. **Adjust Settings**: Enable/disable metadata, thumbnails, playlists
4. **Start Download**: Click "Start" button to begin processing
5. **Monitor Progress**: Watch real-time progress bars and logs
6. **Review Results**: Check log for success/failure messages

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+O` | Open URLs from file |
| `Ctrl+S` | Save log to file |
| `Ctrl+C` | Copy selected text |
| `Ctrl+V` | Paste from clipboard |
| `Ctrl+X` | Cut selected text |
| `Ctrl+A` | Select all text |
| `Alt+F4` | Exit application |

### GUI Requirements

The GUI uses Python's built-in `tkinter` module, which is included with most Python installations.

**If tkinter is not installed:**

<details>
<summary><b>Windows</b></summary>

Tkinter is included by default. If missing, reinstall Python with "tcl/tk" option checked.
</details>

<details>
<summary><b>macOS</b></summary>

```bash
# Usually included with Python
# If missing, install Python from python.org or use Homebrew
brew install python-tk@3.12
```
</details>

<details>
<summary><b>Linux (Ubuntu/Debian)</b></summary>

```bash
sudo apt-get install python3-tk
```
</details>

### GUI Screenshots

*Coming soon: Screenshots of the desktop application in action*

---

## Using Makefile

The project includes a comprehensive **Makefile** for streamlined operations. This is the recommended workflow for development and usage.

### Quick Reference

#### Installation
```bash
make install          # Install package with dependencies
make install-dev      # Install with development tools
make pipx-install     # Install globally via pipx
```

#### Downloads
```bash
make run URL='<url>'                          # Download single video
make run URL='<url>' ARGS='-q high -f flac'   # With custom options
make batch FILE='urls.txt'                    # Batch download
make dry-run URL='<url>'                      # Preview without downloading
```

#### Development & Testing
```bash
make test            # Run all tests
make smoke-test      # Quick validation tests
make coverage        # Generate coverage report
make lint            # Check code quality
make format          # Auto-format code
make check           # Run all quality checks
```

#### Build & Distribution
```bash
make clean           # Remove build artifacts
make build           # Build distribution packages
make publish         # Publish to PyPI
```

<details>
<summary><b>Complete Makefile Command Reference</b></summary>

| Command | Purpose |
|---------|---------|
| **Installation** | |
| `make install` | Install package with dependencies |
| `make install-dev` | Install with development tools |
| `make pipx-install` | Install globally via pipx |
| `make pipx-uninstall` | Remove global installation |
| **Downloads** | |
| `make run URL=<url> [ARGS=...]` | Download single video with optional arguments |
| `make batch FILE=<file> [ARGS=...]` | Download from batch file |
| `make dry-run URL=<url>` | Preview download without processing |
| **Testing & Quality** | |
| `make test` | Run complete test suite |
| `make smoke-test` | Run quick validation tests |
| `make coverage` | Generate HTML coverage report |
| `make lint` | Check code style and quality |
| `make format` | Auto-format code (black, isort) |
| `make security` | Run security scans (bandit, safety) |
| `make check` | Run all quality checks |
| `make validate` | Validate project structure |
| **Build & Deploy** | |
| `make clean` | Remove build artifacts and cache |
| `make build` | Build distribution packages |
| `make publish` | Publish to PyPI |
| **Utilities** | |
| `make help` | Show all available commands |
| `make show-config` | Display current configuration |
| `make version` | Show installed version |
| `make watch` | Auto-run tests on file changes |
| `make pre-commit` | Setup git pre-commit hooks |

</details>

---

## Multi-Platform Plugin System

The downloader supports **9+ popular platforms** through an extensible plugin architecture, providing a unified interface for all media sources.

### Supported Platforms

<table>
<thead>
<tr>
<th>Platform</th>
<th>Features</th>
<th>Playlist</th>
<th>Auth</th>
<th>Formats</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>YouTube</strong></td>
<td>Videos, Shorts, Music</td>
<td align="center">✅</td>
<td align="center">Optional</td>
<td>MP3, MP4, M4A, WAV, OGG, FLAC</td>
</tr>
<tr>
<td><strong>TikTok</strong></td>
<td>Videos, Clips</td>
<td align="center">✅</td>
<td align="center">❌</td>
<td>MP3, MP4, M4A</td>
</tr>
<tr>
<td><strong>Instagram</strong></td>
<td>Posts, Reels, Stories</td>
<td align="center">❌</td>
<td align="center">❌</td>
<td>MP3, MP4, M4A</td>
</tr>
<tr>
<td><strong>SoundCloud</strong></td>
<td>Tracks, Playlists</td>
<td align="center">✅</td>
<td align="center">❌</td>
<td>MP3, M4A, OGG, WAV</td>
</tr>
<tr>
<td><strong>Spotify</strong></td>
<td>Tracks, Playlists, Albums</td>
<td align="center">✅</td>
<td align="center">❌</td>
<td>MP3, M4A, OGG, WAV, FLAC</td>
</tr>
<tr>
<td><strong>Twitch</strong></td>
<td>VODs, Clips, Highlights</td>
<td align="center">❌</td>
<td align="center">❌</td>
<td>MP3, MP4, M4A</td>
</tr>
<tr>
<td><strong>Dailymotion</strong></td>
<td>Videos, Playlists</td>
<td align="center">✅</td>
<td align="center">❌</td>
<td>MP3, MP4, M4A</td>
</tr>
<tr>
<td><strong>Vimeo</strong></td>
<td>Videos, Channels</td>
<td align="center">✅</td>
<td align="center">❌</td>
<td>MP3, MP4, M4A</td>
</tr>
<tr>
<td><strong>Reddit</strong></td>
<td>Videos, Posts</td>
<td align="center">❌</td>
<td align="center">❌</td>
<td>MP3, MP4, M4A</td>
</tr>
</tbody>
</table>

### List Available Plugins

View all installed platform plugins and their capabilities:

```bash
python downloader.py --list-plugins
```

**Output includes:**
- Platform name and description
- Supported content types (audio, video)
- Available output formats
- Playlist support status
- Authentication requirements

### Usage Examples

```bash
# Download from TikTok
python downloader.py https://www.tiktok.com/@creator/video/123456789

# Extract audio from Instagram Reel
python downloader.py -f mp3 https://www.instagram.com/reel/ABC123/

# Download SoundCloud track in high quality
python downloader.py -q high https://soundcloud.com/artist/track-name

# Get Spotify playlist as FLAC files
python downloader.py -p -q best -f flac https://open.spotify.com/playlist/PLAYLIST_ID

# Download Twitch VOD
python downloader.py https://www.twitch.tv/videos/1234567890

# Extract audio from Vimeo video
python downloader.py -f mp3 https://vimeo.com/123456789

# Batch download from multiple platforms
python downloader.py -b mixed_urls.txt
```

### Platform-Specific Features

The plugin system provides intelligent platform handling:

- **🔍 Automatic Detection**: Platform identification from URL structure
- **⚙️ Format Optimization**: Best format selection per platform
- **📋 Playlist Support**: Recursive download for supported platforms
- **🎚️ Quality Mapping**: Platform-specific quality preset translation
- **🔄 Error Recovery**: Platform-aware retry logic and fallbacks
- **📊 Metadata Extraction**: Rich metadata including artwork and tags

### Creating Custom Plugins

Extend the downloader with custom platform support by creating a plugin in `plugins/`:

```python
from plugins.base import BaseConverter, PluginCapabilities, ContentType

class MyPlatformConverter(BaseConverter):
    """Custom converter for MyPlatform"""
    
    def get_capabilities(self) -> PluginCapabilities:
        return PluginCapabilities(
            name="MyPlatform Converter",
            version="1.0.0",
            platform="MyPlatform",
            description="Download media from MyPlatform",
            supported_content_types=[ContentType.AUDIO, ContentType.VIDEO],
            supported_formats=["mp3", "mp4", "m4a"],
            supports_playlists=True,
            requires_authentication=False
        )
    
    def can_handle(self, url: str) -> bool:
        """Check if this converter can handle the URL"""
        return "myplatform.com" in url.lower()
    
    def download(self, url: str, output_path: str, quality: str = 'medium', 
                 format: str = 'mp3', **kwargs):
        """Implement download logic"""
        # Your implementation here
        pass
```

**Register the plugin** in [plugins/\_\_init\_\_.py](plugins/__init__.py):

```python
from .my_platform import MyPlatformConverter

def register_default_plugins():
    registry = get_global_registry()
    registry.register('myplatform', MyPlatformConverter())
    # ... other registrations
```

📚 **See** [PLUGIN_API.md](PLUGIN_API.md) for complete plugin development documentation.

---

## Usage

### Audio Quality Options

| Preset | Bitrate | Typical Use Case |
|--------|---------|------------------|
| `low` | 128 kbps | Audiobooks, podcasts |
| `medium` | 192 kbps | General listening (default) |
| `high` | 320 kbps | High-quality music |
| `best` | Original | Archival, maximum quality |

```bash
python downloader.py -q high <url>
```

### Supported Audio Formats

```bash
python downloader.py -f mp3 <url>    # MP3 (default)
python downloader.py -f m4a <url>    # M4A
python downloader.py -f flac <url>   # FLAC (lossless)
python downloader.py -f wav <url>    # WAV (lossless)
python downloader.py -f ogg <url>    # OGG Vorbis
```

### Playlist Processing

```bash
# Download entire playlist
python downloader.py -p <playlist_url>

# Download playlist with specific quality
python downloader.py -p -q high -f flac <playlist_url>
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
python downloader.py -b urls.txt

# With quality and output directory
python downloader.py -b urls.txt -q best -o ./music

# With retry and logging
python downloader.py -b urls.txt --retries 5 --log-file download.log

# Stop on first failure
python downloader.py -b urls.txt --fail-fast

# Stop after N failures
python downloader.py -b urls.txt --max-failures 3
```

### Output and Naming

```bash
# Custom output directory
python downloader.py -o ~/Music <url>

# Custom filename template
python downloader.py -t "%(artist)s - %(title)s" <url>
python downloader.py -t "%(uploader)s - %(upload_date)s - %(title)s" <url>
```

Available variables: `%(title)s`, `%(artist)s`, `%(uploader)s`, `%(upload_date)s`, `%(id)s`, `%(ext)s`

### Dry-Run Mode

Preview downloads without processing:

```bash
python downloader.py --dry-run <url>
python downloader.py --dry-run -b urls.txt
```

### Configuration Management

```bash
# Display current configuration
python downloader.py --show-config

# Save configuration to file
python downloader.py --save-config
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
python downloader.py <url>

# Disable archive
python downloader.py --no-archive <url>

# Use custom archive file
python downloader.py --archive /path/to/archive <url>
```

### Logging

Enable detailed logging for debugging:

```bash
python downloader.py -b urls.txt --log-file download.log
```

### Network Options

```bash
# HTTP proxy
python downloader.py --proxy http://user:pass@host:port <url>

# SOCKS5 proxy
python downloader.py --proxy socks5://127.0.0.1:1080 <url>

# Rate limiting
python downloader.py --limit-rate 1M <url>

# Cookie authentication
python downloader.py --cookies cookies.txt <url>
```

### Error Handling

```bash
# Custom retry attempts
python downloader.py --retries 5 <url>

# Skip validation checks
python downloader.py --skip-checks <url>

# Disable metadata and thumbnails
python downloader.py --no-metadata --no-thumbnail <url>
```

## Command Reference

```
usage: downloader.py [-h] [-q {low,medium,high,best}] 
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
python downloader.py -o ~/Downloads <url>
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
python downloader.py -b urls.txt --log-file debug.log
```

Increase retry attempts:
```bash
python downloader.py -b urls.txt --retries 5
```

### Video marked as "already downloaded"
Force re-download:
```bash
python downloader.py --no-archive <url>
```

Or clear archive:
```bash
rm ~/.ytdownloader_archive.txt
```

## Project Structure

```
youtube_mp3_downloader/
├── downloader.py              # Main application
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

This project is licensed under the GNU General Public License v3.0 or later — see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## Acknowledgments

This project uses:
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — YouTube extraction and download
- [rich](https://github.com/Textualize/rich) — Rich terminal output
- [FFmpeg](https://ffmpeg.org/) — Audio processing and conversion
