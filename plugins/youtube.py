"""
YouTube converter plugin - wrapper around yt-dlp's native YouTube support.
"""

import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yt_dlp
from yt_dlp.utils import DownloadError

from .base import BaseConverter, ContentType, ExtractorType, PluginCapabilities

ANSI_ESCAPE = re.compile(r"\x1b\[[0-9;]*m")

FALLBACK_HTTP_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.youtube.com/",
}


def _strip_ansi(text: str) -> str:
    """Remove ANSI color codes from error strings for UI display and parsing."""
    return ANSI_ESCAPE.sub("", text or "")


def _is_forbidden_error(message: str) -> bool:
    """Detect YouTube 403 blocks that benefit from fallback settings."""
    msg = (message or "").lower()
    return (
        "http error 403" in msg
        or "403: forbidden" in msg
        or "unable to download video data" in msg
        or ("http error" in msg and "forbidden" in msg)
    )


def _merge_ydl_opts(base: Dict[str, Any], extra: Dict[str, Any]) -> Dict[str, Any]:
    """Merge nested yt-dlp options (headers/extractor_args) safely."""
    merged = dict(base)
    for key, value in extra.items():
        if key in ("extractor_args", "http_headers") and isinstance(
            value, dict
        ) and isinstance(merged.get(key), dict):
            merged[key] = {**merged[key], **value}
        else:
            merged[key] = value
    return merged


class YouTubeConverter(BaseConverter):
    """YouTube audio and video downloader"""

    def get_capabilities(self) -> PluginCapabilities:
        return PluginCapabilities(
            name="YouTube Converter",
            version="1.5.2",
            platform="YouTube",
            description="Download audio and video from YouTube videos, playlists, and shorts",
            author="YouTube MP3 Downloader",
            url_patterns=[
                r"^https?://(www\.)?youtube\.com/watch\?v=[\w-]+",
                r"^https?://(www\.)?youtube\.com/playlist\?list=[\w-]+",
                r"^https?://youtu\.be/[\w-]+",
                r"^https?://(www\.)?youtube\.com/shorts/[\w-]+",
                r"^https?://music\.youtube\.com/watch\?v=[\w-]+",
            ],
            supported_content_types=[
                ContentType.AUDIO,
                ContentType.VIDEO,
                ContentType.MIXED,
            ],
            supports_playlist=True,
            supports_auth=True,
            supports_subtitles=True,
            supports_metadata=True,
            extractor_type=ExtractorType.YT_DLP,
            quality_presets=["low", "medium", "high", "best"],
            output_formats=["mp3", "mp4", "m4a", "wav", "ogg", "flac"],
        )

    def can_handle(self, url: str) -> bool:
        """Check if URL is a YouTube URL"""
        for pattern in self.capabilities.url_patterns:
            if re.match(pattern, url, re.IGNORECASE):
                return True
        return False

    def validate_url(self, url: str) -> Tuple[bool, str]:
        """Validate YouTube URL format"""
        if not url:
            return False, "URL cannot be empty"

        if self.can_handle(url):
            return True, ""

        return False, f"Invalid YouTube URL format: {url}"

    def get_info(self, url: str, **kwargs) -> Dict[str, Any]:
        """Extract metadata from YouTube URL"""
        try:
            ydl_opts = {
                "quiet": True,
                "no_warnings": True,
                "noplaylist": not kwargs.get("is_playlist", False),
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

                return {
                    "title": info.get("title", "Unknown"),
                    "duration": info.get("duration", 0),
                    "thumbnail": info.get("thumbnail", None),
                    "uploader": info.get("uploader", "Unknown"),
                    "description": info.get("description", ""),
                    "view_count": info.get("view_count", 0),
                    "like_count": info.get("like_count", 0),
                    "upload_date": info.get("upload_date", ""),
                    "is_playlist": "entries" in info,
                    "video_count": (
                        len(info.get("entries", [])) if "entries" in info else 1
                    ),
                    "entries": info.get("entries"),
                }
        except Exception as e:
            raise RuntimeError(f"Failed to extract YouTube info: {e}")

    def download(
        self,
        url: str,
        output_path: str,
        quality: str = "medium",
        format: str = "mp3",
        **kwargs,
    ) -> Tuple[bool, Optional[str], Optional[str]]:
        """Download and convert YouTube content"""
        try:
            Path(output_path).mkdir(parents=True, exist_ok=True)
            filename_template = kwargs.get("filename_template", "%(title)s.%(ext)s")
            outtmpl = str(Path(output_path) / filename_template)

            # Quality bitrates
            bitrates = {
                "low": "128",
                "medium": "192",
                "high": "320",
                "best": "0",
            }
            bitrate = bitrates.get(quality, "192")

            postprocessors = [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": format,
                    "preferredquality": bitrate,
                }
            ]

            if kwargs.get("embed_metadata", True):
                postprocessors.append({"key": "FFmpegMetadata"})

            if kwargs.get("embed_thumbnail", True):
                postprocessors.append({"key": "EmbedThumbnail"})

            progress_hook = kwargs.get("progress_hook") or kwargs.get(
                "progress_callback"
            )
            cancel_event = kwargs.get("cancel_event")

            ydl_opts: Dict[str, Any] = {
                "format": "bestaudio/best",
                "postprocessors": postprocessors,
                "outtmpl": outtmpl,
                "quiet": kwargs.get("quiet", False),
                "no_warnings": kwargs.get("quiet", False),
                "writethumbnail": kwargs.get("embed_thumbnail", True),
                "noplaylist": not kwargs.get("is_playlist", False),
                "continuedl": True,
            }

            # Add optional parameters
            if kwargs.get("proxy"):
                ydl_opts["proxy"] = kwargs["proxy"]
            if kwargs.get("cookies_file"):
                ydl_opts["cookiefile"] = kwargs["cookies_file"]
            if kwargs.get("rate_limit"):
                ydl_opts["ratelimit"] = kwargs["rate_limit"]
            if kwargs.get("archive_file"):
                ydl_opts["download_archive"] = kwargs["archive_file"]
            if kwargs.get("skip_existing"):
                ydl_opts["nooverwrites"] = True

            max_retries = kwargs.get("max_retries")
            if max_retries is not None:
                try:
                    retries = max(0, int(max_retries))
                except (TypeError, ValueError):
                    retries = 0
                ydl_opts["retries"] = retries
                ydl_opts["fragment_retries"] = retries

            downloaded_file = None
            any_downloaded = False

            class ProgressHook:
                def __call__(self, d):
                    nonlocal downloaded_file
                    nonlocal any_downloaded
                    if cancel_event and cancel_event.is_set():
                        raise DownloadError("Download cancelled by user")
                    if d["status"] == "finished":
                        downloaded_file = d.get("filename")
                        any_downloaded = True

            hooks = [ProgressHook()]
            if progress_hook:
                hooks.append(progress_hook)
            ydl_opts["progress_hooks"] = hooks

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                if not any_downloaded:
                    return (
                        False,
                        None,
                        "Skipped: no new files downloaded (already exists or in archive).",
                    )
                return True, downloaded_file, None
            except Exception as e:
                error_message = _strip_ansi(str(e))
                if _is_forbidden_error(error_message):
                    fallback_opts = _merge_ydl_opts(
                        ydl_opts,
                        {
                            "extractor_args": {
                                "youtube": {"player_client": ["android", "web"]}
                            },
                            "http_headers": FALLBACK_HTTP_HEADERS,
                        },
                    )
                    try:
                        with yt_dlp.YoutubeDL(fallback_opts) as ydl:
                            ydl.download([url])
                        if not any_downloaded:
                            return (
                                False,
                                None,
                                "Skipped: no new files downloaded (already exists or in archive).",
                            )
                        return True, downloaded_file, None
                    except Exception as fallback_error:
                        fallback_message = _strip_ansi(str(fallback_error))
                        hint = (
                            "Hint: YouTube blocked the request (HTTP 403). "
                            "Try providing a cookies file or updating yt-dlp."
                        )
                        if _is_forbidden_error(fallback_message):
                            fallback_message = f"{fallback_message} ({hint})"
                        return False, None, f"YouTube download failed: {fallback_message}"
                return False, None, f"YouTube download failed: {error_message}"

        except Exception as e:
            return False, None, f"YouTube download failed: {_strip_ansi(str(e))}"
