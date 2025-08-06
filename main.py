from gemini_api.client import generate_content
from youtube_utils.transcriber import download_subtitles

if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=UtSSMs6ObqY'
    download_subtitles(video_url, lang='en')