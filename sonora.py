import re
import subprocess
import sys
import yt_dlp

BANNER = """███████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗
██╔════╝██╔═══██╗████╗  ██║██╔═══██╗██╔══██╗██╔══██╗
███████╗██║   ██║██╔██╗ ██║██║   ██║██████╔╝███████║
╚════██║██║   ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██║
███████║╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║██║  ██║
╚══════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝"""


class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    GRAY = "\033[90m"


def enable_ansi():
    if sys.platform == "win32":
        try:
            import ctypes

            ctypes.windll.kernel32.SetConsoleMode(
                ctypes.windll.kernel32.GetStdHandle(-11), 7
            )
        except Exception:
            pass


def set_title(title):
    if sys.platform == "win32":
        try:
            import ctypes

            ctypes.windll.kernel32.SetConsoleTitleW(title)
        except Exception:
            pass


def out(text, color=Color.RESET, bold=False, end="\n"):
    prefix = Color.BOLD if bold else ""
    print(f"{prefix}{color}{text}{Color.RESET}", end=end)


def prompt(text):
    return input(f"{Color.CYAN}{text}{Color.RESET}")


def separator():
    out("=" * 60, Color.DIM)


def success(text):
    out(text, Color.GREEN, bold=True)


def error(text):
    out(text, Color.RED, bold=True)


def warn(text):
    out(text, Color.YELLOW)


def info(text):
    out(text, Color.GRAY)


def select_format():
    warn("Choose output format:")
    out("  1) FLAC (lossless) [default]", Color.CYAN)
    out("  2) MP3 320kbps", Color.CYAN)
    choice = prompt("> Select format (1 or 2, press Enter for FLAC): ").strip()
    return "flac" if choice != "2" else "mp3"


def download_youtube(url, fmt):
    postprocessor = {'key': 'FFmpegExtractAudio', 'preferredcodec': fmt}
    if fmt == 'mp3':
        postprocessor['preferredquality'] = '320'

    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [postprocessor],
    }

    info("Downloading from YouTube...")
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])

    success(f"{fmt.upper()} downloaded successfully.")


def download_spotify(url, fmt):
    args = [sys.executable, "-m", "spotdl", url, "--format", fmt]
    if fmt == "mp3":
        args += ["--bitrate", "320k"]

    result = subprocess.run(args)

    if result.returncode != 0:
        raise RuntimeError("spotDL failed. Make sure it is installed: pip install spotdl")


def download(url, fmt):
    if re.match(r"https?://(open\.)?spotify\.com/", url, re.IGNORECASE):
        download_spotify(url, fmt)
    elif re.match(r"https?://(www\.)?(youtube\.com|youtu\.be)/", url, re.IGNORECASE):
        download_youtube(url, fmt)
    else:
        raise ValueError("Unsupported link. Please provide a YouTube or Spotify link.")


def main():
    enable_ansi()
    set_title("SONORA")

    out(BANNER, Color.CYAN, bold=True)
    out("-------- YouTube & Spotify audio downloader --------", Color.CYAN, bold=True)
    separator()

    fmt = select_format()
    info(f"Output format: {fmt.upper()}")
    separator()

    while True:
        try:
            url = prompt("> Paste a link (YouTube or Spotify) or type 'exit' to quit: ").strip()
        except KeyboardInterrupt:
            print()
            break

        if url.lower() in ("exit", "quit", "q"):
            break

        if not url:
            warn("No link provided. Try again.")
            continue

        try:
            download(url, fmt)
        except Exception as e:
            error(f"Error: {e}")

        separator()

    out("Goodbye!", Color.CYAN, bold=True)


if __name__ == "__main__":
    main()