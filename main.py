import yt_dlp

link = input("Enter the link: ")

ydl_opts = {
        'format': 'bestvideo+bestaudio',
    'outtmpl': '%(title)s.%(ext)s',
    'quiet': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(link, download=False)
    ydl.download([link])
    print(f"'{info['title']}' downloaded!")
