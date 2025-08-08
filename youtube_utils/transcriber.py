from youtube_transcript_api import YouTubeTranscriptApi

import yt_dlp

def get_video_title(video_url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        return info.get('title', 'No Title Found')

def get_transcript(video_url):
    """
    Fetch the transcript for a given YouTube video ID.
    :param video_id: The ID of the YouTube video.
    :return: The transcript of the video.
    """
    title = get_video_title(video_url)
    video_id = video_url.split('v=')[-1] if 'v=' in video_url else video_url.split('/')[-1]

    transcript = {}
    try:
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(video_id, languages=['en', 'id'])

        for snippet in fetched_transcript:
            transcript[snippet.start] = snippet.text

        return title, transcript
    
    except Exception as e:
        print("Error:", e)



