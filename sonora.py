import yt_dlp

url = input("Pega el enlace de YouTube: ")

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
    print(f"\nError: {e}")rint(f"\nError: {e}")