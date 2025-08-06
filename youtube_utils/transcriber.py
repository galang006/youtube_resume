import yt_dlp

def download_subtitles(video_url, lang='en'):
    ydl_opts = {
        'skip_download': True,  # Don't download video
        'writeautomaticsub': True, 
        'writesubtitles': True,
        'subtitleslangs': [lang],
        'subtitlesformat': 'vtt',  # or 'srt' if you prefer
        'outtmpl': '%(title)s.%(ext)s',
        'ratelimit': 100000, 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        title = info.get('title', 'video')
        print(f"Subtitles downloaded for: {title}")

# Example usage
video_url = 'https://www.youtube.com/watch?v=UtSSMs6ObqY'
download_subtitles(video_url, lang='en') 