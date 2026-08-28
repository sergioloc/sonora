import re
import subprocess
import sys
import yt_dlp

url = input("Pega el enlace de YouTube o Spotify: ").strip()

if re.match(r"https?://(open\.)?spotify\.com/", url, re.IGNORECASE):
    print("Enlace de Spotify detectado. Usando spotDL...")
    resultado = subprocess.run(
        [sys.executable, "-m", "spotdl", url, "--format", "mp3", "--bitrate", "192k"]
    )
    if resultado.returncode == 0:
        print("\nMP3 descargado correctamente.")
    else:
        print("\nError: no se pudo descargar. Revisa que spotdl y ffmpeg esten instalados.")

elif re.match(r"https?://(www\.)?(youtube\.com|youtu\.be)/", url, re.IGNORECASE):
    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])

        print("\nMP3 descargado correctamente.")

    except Exception as e:
        print(f"\nError: {e}")

else:
    print("No se reconoce el enlace. Debe ser de YouTube o Spotify.")rint(f"\nError: {e}")