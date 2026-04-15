import yt_dlp

url = input("Enter the url: ")

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegVideoRemuxer',
        'preferedformat': 'mp4',
    }],

    'outtmpl': 'downloaded-videos/%(title)s.%(ext)s',
    'quiet': True
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        ydl.download([url])
        print(f"'{info['title']}' downloaded!")
        
except Exception as e:
    print(f'An error has occured: {e}')