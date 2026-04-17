import yt_dlp
import sys
import os

def get_base_path():
    if getattr(sys, 'frozen', False):  # running as exe
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))  # running as script

def main():
    url = input("Enter the url: ")

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegVideoRemuxer',
            'preferedformat': 'mp4',
        }],
        'outtmpl': 'downloaded-videos/%(title)s.%(ext)s',
        'ffmpeg_location': get_base_path(),
        'quiet': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"Downloading: '{info['title']}'...")
            ydl.download([url])
            print(f"'{info['title']}' downloaded successfully!")

    except Exception as e:
        print(f'An error has occurred: {e}')

    input("Press Enter to exit...")

if __name__ == '__main__':
    main()
