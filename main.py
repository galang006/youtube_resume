from gemini_api.client import generate_content
from youtube_utils.transcriber import get_transcript
import os
import re

def clean_filename(filename):
    # Hapus karakter ilegal di Windows: \ / : * ? " < > |
    return re.sub(r'[\\/:*?"<>|]', '_', filename)

if __name__ == "__main__":
    output_dir = "./resume"
    os.makedirs(output_dir, exist_ok=True)

    video_url = input("Enter YouTube video URL: ")

    print(f"Get Transcript for video...")
    title, transcript = get_transcript(video_url)
    
    if not transcript:
        print("Transcript not available.")
        exit()

    print(f"Generating summary for video: {title}")
    response = generate_content(transcript)

    title_clean = clean_filename(title)
    output_file = f"{output_dir}/{title_clean}.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(response)

    print(f"Summary saved to {output_file}")
    