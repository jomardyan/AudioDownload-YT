# YouTube MP3 Downloader - Enhanced

A powerful and user-friendly Python script to download audio from YouTube videos and playlists as MP3/FLAC/M4A files with quality options, metadata embedding, and batch processing.

## ✨ Features

- 🎵 **Multiple Quality Presets**: Low (128k), Medium (192k), High (320k), Best (original)
- 🎼 **Multiple Audio Formats**: MP3, M4A, FLAC, WAV, OGG
- 📋 **Playlist Support**: Download entire playlists with one command
- 📁 **Batch Downloads**: Process multiple URLs from a text file
- 🎨 **Enhanced Progress Display**: Beautiful progress bars with download speed and ETA
- 📝 **Metadata Embedding**: Automatic ID3 tags and album artwork
- 🎯 **Custom Output**: Configurable output directories and filename templates
- 🎨 **Color-Coded Output**: Easy-to-read console messages with status indicators

## Requirements

- Python 3.6+
- ffmpeg (for audio conversion)

## Installation

1. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

2. **Install ffmpeg** (if not already installed):
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

## Usage

### Basic Usage

Download a single video with default settings (medium quality MP3):
```bash
python youtube_mp3_downloader.py <youtube_url>
```

### Quality Options

Download with different quality presets:
```bash
# Low quality (128 kbps) - smaller file size
python youtube_mp3_downloader.py -q low <url>

# Medium quality (192 kbps) - default
python youtube_mp3_downloader.py -q medium <url>

# High quality (320 kbps) - better audio
python youtube_mp3_downloader.py -q high <url>

# Best quality (original) - highest quality
python youtube_mp3_downloader.py -q best <url>
```

### Audio Format Options

Download in different audio formats:
```bash
# MP3 format (default)
python youtube_mp3_downloader.py -f mp3 <url>

# M4A format
python youtube_mp3_downloader.py -f m4a <url>

# FLAC format (lossless)
python youtube_mp3_downloader.py -f flac <url>

# WAV format
python youtube_mp3_downloader.py -f wav <url>

# OGG format
python youtube_mp3_downloader.py -f ogg <url>
```

### Playlist Downloads

Download entire playlists:
```bash
python youtube_mp3_downloader.py -p <playlist_url>

# With custom quality and format
python youtube_mp3_downloader.py -p -q high -f flac <playlist_url>
```

### Batch Downloads

Create a text file with URLs (one per line):
```
# urls.txt
https://www.youtube.com/watch?v=VIDEO_ID_1
https://www.youtube.com/watch?v=VIDEO_ID_2
https://www.youtube.com/playlist?list=PLAYLIST_ID
# Lines starting with # are ignored
```

Download all URLs from the file:
```bash
python youtube_mp3_downloader.py -b urls.txt

# With custom settings
python youtube_mp3_downloader.py -b urls.txt -q best -o ./my_music
```

### Custom Output Directory

Specify where to save downloaded files:
```bash
python youtube_mp3_downloader.py -o ./my_music <url>
python youtube_mp3_downloader.py --output /path/to/music <url>
```

### Custom Filename Templates

Customize output filename format:
```bash
# Artist - Title format
python youtube_mp3_downloader.py -t "%(artist)s - %(title)s" <url>

# Include upload date
python youtube_mp3_downloader.py -t "%(upload_date)s - %(title)s" <url>

# Channel name included
python youtube_mp3_downloader.py -t "%(uploader)s - %(title)s" <url>
```

Available template variables:
- `%(title)s` - Video title
- `%(artist)s` - Artist name (if available)
- `%(uploader)s` - Channel/uploader name
- `%(upload_date)s` - Upload date
- `%(id)s` - Video ID
- `%(ext)s` - File extension

### Advanced Options

Disable metadata embedding:
```bash
python youtube_mp3_downloader.py --no-metadata <url>
```

Disable thumbnail embedding:
```bash
python youtube_mp3_downloader.py --no-thumbnail <url>
```

Quiet mode (minimal output):
```bash
python youtube_mp3_downloader.py --quiet <url>
```

### Combined Examples

High-quality FLAC with custom output:
```bash
python youtube_mp3_downloader.py -q best -f flac -o ./music/albums <url>
```

Batch download with high quality and custom template:
```bash
python youtube_mp3_downloader.py -b urls.txt -q high -t "%(artist)s - %(title)s" -o ./music
```

Download playlist without metadata:
```bash
python youtube_mp3_downloader.py -p --no-metadata --no-thumbnail <playlist_url>
```

## Command-Line Options

```
usage: youtube_mp3_downloader.py [-h] [-q {low,medium,high,best}] 
                                  [-f {mp3,m4a,flac,wav,ogg}]
                                  [-o OUTPUT] [-t TEMPLATE] [-p] [-b BATCH_FILE]
                                  [--no-metadata] [--no-thumbnail] [--quiet]
                                  [url]

Options:
  url                           YouTube video or playlist URL
  -q, --quality                 Audio quality: low, medium, high, best (default: medium)
  -f, --format                  Audio format: mp3, m4a, flac, wav, ogg (default: mp3)
  -o, --output                  Output directory (default: ./downloads)
  -t, --template                Filename template (default: %(title)s.%(ext)s)
  -p, --playlist                Download entire playlist
  -b, --batch-file              Download from batch file (one URL per line)
  --no-metadata                 Do not embed metadata
  --no-thumbnail                Do not embed thumbnail as album art
  --quiet                       Suppress output messages
  -h, --help                    Show this help message and exit
```

## Quality Guide

| Preset | Bitrate | File Size | Use Case |
|--------|---------|-----------|----------|
| low    | 128 kbps | ~1 MB/min | Audiobooks, podcasts, saving space |
| medium | 192 kbps | ~1.5 MB/min | General music listening |
| high   | 320 kbps | ~2.5 MB/min | High-quality music |
| best   | Original | Varies | Archival, best possible quality |

## Format Guide

| Format | Type | Quality | Compatibility |
|--------|------|---------|---------------|
| MP3    | Lossy | Good | Universal - all devices |
| M4A    | Lossy | Better | Apple devices, modern players |
| FLAC   | Lossless | Perfect | Audiophile, archival |
| WAV    | Lossless | Perfect | Professional audio work |
| OGG    | Lossy | Good | Open source preference |

## Troubleshooting

**Error: No module named 'yt_dlp'**
```bash
pip install -r requirements.txt
```

**Error: FFmpeg not found**
- Install ffmpeg using the installation instructions above

**Error: Permission denied**
- Make sure you have write permissions to the output directory
- Try using a different output directory with `-o`

**Downloads are slow**
- This is normal for high-quality/large files
- Consider using a lower quality preset for faster downloads

**Playlist not downloading**
- Make sure to use the `-p` flag for playlists
- Verify the playlist URL is correct and public

## Files and Directories

- `youtube_mp3_downloader.py` - Main script
- `requirements.txt` - Python dependencies
- `downloads/` - Default output directory for downloaded files

## Notes

- Downloaded files are saved in the `downloads` folder by default
- Metadata includes title, artist, album art (thumbnail), and other available information
- Progress bars show download speed, percentage, and estimated time remaining
- Batch processing continues even if individual downloads fail
- All output paths are created automatically if they don't exist

## License

Free to use and modify for personal and educational purposes.
