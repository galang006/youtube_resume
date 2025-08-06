from gemini_api.client import generate_content
from youtube_utils.transcriber import get_transcript

if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=UtSSMs6ObqY'
    transcript = get_transcript(video_url)

    contents = str(transcript) + "\nThis is dict with format {'key': 'value'} = {'timestamp start the substitle': 'subtitle text'}. make resume from this transcript."

    response = generate_content(contents)

    print(response)

    