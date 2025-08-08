from gemini_api.client import generate_content
from youtube_utils.transcriber import get_transcript

if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=UtSSMs6ObqY'
    transcript = get_transcript(video_url)

    response = generate_content(transcript)

    print(response)

    