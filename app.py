import streamlit as st
from gemini_api.client import generate_content
from youtube_utils.transcriber import get_transcript
import time
import re

def clean_filename(filename):
    return re.sub(r'[\\/:*?"<>|]', '_', filename)

st.set_page_config(page_title="YouTube Video Summarizer", page_icon="🎥", layout="centered")

st.title("🎥 YouTube Video Summarizer with Gemini API")
st.write("Enter the YouTube link and get an automatic summary using Gemini API.")

language_options = {
    "Indonesian": "Indonesian",
    "English": "English",
    "Japanese": "Japanese",
    "Korean": "Korean",
    "Spanish": "Spanish",
    "Arabic": "Arabic"
}
target_lang = st.selectbox("🌍 Translate the summary results into:", list(language_options.keys()))

video_url = st.text_input("Enter the YouTube URL", placeholder="https://www.youtube.com/watch?v=UtSSMs6ObqY")

if st.button("Create a Summary"):
    if not video_url.strip():
        st.error("❌ YouTube URL cannot be empty!")
    else:
        try:
            progress = st.progress(0)
            status_text = st.empty()

            status_text.text("📄 Take video transcript...")
            title, transcript = get_transcript(video_url)
            if not transcript:
                st.error("❌ Failed to retrieve video transcript!")
                st.stop()
            time.sleep(1)
            progress.progress(30)

            status_text.text("🤖 Send to Gemini API to create a summary...")
            summary = generate_content(transcript)
            progress.progress(60)

            status_text.text(f"🌍 Translate summary into {target_lang}...")
            translate_prompt = f"Translate this text to {language_options[target_lang]}:\n\n{summary}"
            translated_summary = generate_content(translate_prompt)
            progress.progress(100)

            status_text.text("✅ Summary completed!")
            st.subheader(f"📌 {title}")
            st.write(translated_summary)
            
            title_clean = clean_filename(title)
            st.download_button(
                label="📥 Download Ringkasan",
                data=translated_summary,
                file_name=f"{title_clean}_summary.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"An error occured: {e}")