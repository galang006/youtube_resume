from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_url):
    """
    Fetch the transcript for a given YouTube video ID.
    :param video_id: The ID of the YouTube video.
    :return: The transcript of the video.
    """
    video_id = video_url.split('v=')[-1] if 'v=' in video_url else video_url.split('/')[-1]

    transcript = {}
    try:
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(video_id, languages=['en'])

        for snippet in fetched_transcript:
            transcript[snippet.start] = snippet.text

        return transcript
    
    except Exception as e:
        print("Error:", e)



