# Python Library Usage Guide

TubeTracks can be used as a Python library to integrate media downloading capabilities directly into your own applications.

## Installation

First, install the package from PyPI:

```bash
pip install tubetracks
```

## Basic Usage

The core functionality is exposed through the `downloader` module. The main entry point is the `download_audio` function.

### Downloading a Single Video

```python
from downloader import download_audio

# Simple download with default settings
result = download_audio("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if result.success:
    print(f"Downloaded to: {result.output_path}")
else:
    print(f"Error: {result.error_message}")
```

### Customizing Download Options

You can customize quality, format, output directory, and more:

```python
from downloader import download_audio

result = download_audio(
    url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    output_dir="./my_music",
    quality="high",       # low, medium, high, best
    audio_format="flac",  # mp3, m4a, flac, wav, ogg
    embed_metadata=True,
    embed_thumbnail=True,
    filename_template="%(artist)s - %(title)s.%(ext)s"
)
```

## Advanced Usage

### Downloading Playlists

To download a playlist, set `is_playlist=True`. You can also control concurrency.

```python
result = download_audio(
    url="https://www.youtube.com/playlist?list=PL...",
    is_playlist=True,
    concurrent_downloads=3,  # Download 3 videos in parallel
    skip_existing=True       # Skip files that already exist
)

print(f"Playlist result: {result.title}")
print(f"Total time: {result.duration_seconds:.2f}s")
```

### Handling Results

The `download_audio` function returns a `DownloadResult` object with detailed information:

```python
from downloader import DownloadResult, ErrorCode

result = download_audio("...")

print(f"Success: {result.success}")
print(f"URL: {result.url}")
print(f"Title: {result.title}")
print(f"Output Path: {result.output_path}")
print(f"Duration: {result.duration_seconds}s")

if not result.success:
    print(f"Error Code: {result.error_code}")  # e.g., ErrorCode.NETWORK_ERROR
    print(f"Error Message: {result.error_message}")
    print(f"Attempts: {result.attempts}")
```

### Progress Tracking

You can track download progress by providing a callback function:

```python
def my_progress_callback(data):
    status = data.get("status")
    
    if status == "downloading":
        percent = (data.get("downloaded_bytes", 0) / data.get("total_bytes", 1)) * 100
        print(f"Progress: {percent:.1f}% - Speed: {data.get('speed')}")
        
    elif status == "finished":
        print(f"Finished: {data.get('filename')}")
        
    elif status == "error":
        print(f"Error: {data.get('error')}")

result = download_audio(
    "https://www.youtube.com/watch?v=...",
    progress_callback=my_progress_callback
)
```

### Using Plugins

The library automatically detects and uses available plugins for supported platforms (TikTok, Instagram, etc.). No special configuration is needed—just pass the URL.

```python
# Download from TikTok
result = download_audio("https://www.tiktok.com/@user/video/...")

# Download from SoundCloud
result = download_audio("https://soundcloud.com/artist/track")
```

## Error Handling

The library uses the `ErrorCode` enum to classify errors:

```python
from downloader import download_audio, ErrorCode

result = download_audio("...")

if not result.success:
    if result.error_code == ErrorCode.NETWORK_ERROR:
        print("Please check your internet connection.")
    elif result.error_code == ErrorCode.NOT_FOUND:
        print("Video not found or deleted.")
    elif result.error_code == ErrorCode.AGE_RESTRICTED:
        print("Video is age restricted.")
```
