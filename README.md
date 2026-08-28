# SONORA

Downloads audio to MP3 (192 kbps) from **YouTube** or **Spotify** links.

It auto-detects the link type and uses the right tool. For Spotify links it uses **spotDL**, which searches the track on YouTube and downloads it with Spotify metadata.

## Dependencies

- **Python 3.8 or higher**
- **yt-dlp** - downloads from YouTube
- **spotdl** - handles Spotify links
- **FFmpeg** - required to convert to MP3

Install the Python packages:

```bash
pip install yt-dlp spotdl
```

### Installing FFmpeg

**Windows** (with winget):

```bash
winget install Gyan.FFmpeg
```

Alternatively, download it from https://ffmpeg.org and add the `bin` folder to your `PATH`.

Optional: `spotdl` can download it for you:

```bash
spotdl --download-ffmpeg
```

## Usage

Run the script:

```bash
python sonora.py
```

(On Windows, if `python` is not on your PATH, use `py sonora.py`.)

Paste a YouTube or Spotify link and press Enter:

```
> Paste a link (YouTube or Spotify) or type 'exit' to quit:
```

You can download multiple links in the same session. Type `exit` (or press `Ctrl+C`) to quit.

The MP3 files are saved in the same folder where the script runs.

## Note

Spotify does not allow downloading its audio directly (DRM), so spotDL searches the same track on YouTube and downloads it, embedding Spotify metadata.
