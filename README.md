# YouTube Video Summarizer

This project provides a simple yet effective way to extract transcripts from YouTube videos and generate concise summaries using the Google Gemini API. It automates the process of fetching video content and transforming it into digestible summaries, making it easy to grasp the main points of long videos quickly.

## Features
-   **YouTube Transcript Extraction**: Fetches timed transcripts from specified YouTube video URLs.
-   **AI-Powered Summarization**: Utilizes the Google Gemini API to generate intelligent and coherent summaries of the fetched transcripts.
-   **Multi-language Support**: Capable of fetching transcripts in both English (`en`) and Indonesian (`id`) languages.
-   **Modular Design**: Structured with separate modules for YouTube utilities and Gemini API interactions, promoting maintainability and clarity.
-   **Environment Variable Configuration**: Securely manages API keys using `.env` files.

## Installation
To set up and run this project on your local machine, follow these steps:

1.  **Obtain the Codebase:**
    Create the project directory and populate it with the provided files:

    ```
    youtube_resume/
    ├── .gitignore
    ├── main.py
    ├── gemini_api/
    │   └── client.py
    └── youtube_utils/
        └── transcriber.py
    ```
    Copy the respective code into each file.

2.  **Create a Virtual Environment (Recommended):**
    It's good practice to use a virtual environment to manage project dependencies.
    ```bash
    python -m venv venv
    # Activate the virtual environment
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies:**
    Install the required Python libraries using pip:
    ```bash
    pip install google-generativeai python-dotenv youtube-transcript-api
    ```

4.  **Set up Google Gemini API Key:**
    To use the Gemini API, you need an API key.
    -   Go to [Google AI Studio](https://aistudio.google.com/).
    -   Create a new API key if you don't have one.
    -   Create a file named `.env` in the root directory of your project (the same directory as `main.py`).
    -   Add your API key to the `.env` file in the following format:
        ```
        GEMINI_KEY="YOUR_GEMINI_API_KEY_HERE"
        ```
        Replace `YOUR_GEMINI_API_KEY_HERE` with your actual Google Gemini API key.

## Usage
Once the installation is complete, you can run the summarizer:

1.  **Specify Video URL:**
    Open `main.py` and modify the `video_url` variable to the YouTube video you wish to summarize:

    ```python
    # main.py
    if __name__ == "__main__":
        video_url = 'https://www.youtube.com/watch?v=0kLvVINbCtk' # <--- Change this URL to your desired video
        transcript = get_transcript(video_url)

        response = generate_content(transcript)

        print(response)
    ```

2.  **Run the Script:**
    Navigate to the project's root directory in your terminal (where `main.py` is located) and execute the script:

    ```bash
    python main.py
    ```

The script will perform the following actions:
-   Fetch the transcript for the specified YouTube video.
-   Send the transcript to the Google Gemini API for summarization.
-   Print the generated summary directly to your console.

## Code Structure
The project is organized into a clear and modular structure to separate functionalities:

-   `main.py`:
    This is the primary entry point of the application. It orchestrates the overall workflow: defining the target YouTube video URL, initiating the transcript fetching process, calling the Gemini API to generate a summary, and finally displaying the result.

-   `gemini_api/`:
    This directory encapsulates modules responsible for interacting with the Google Gemini API.
    -   `client.py`: Contains the `generate_content` function. This function initializes the Gemini client using the API key from the `.env` file, constructs the prompt for summarization using the video transcript, and sends the request to the Gemini API, returning the generated summary.

-   `youtube_utils/`:
    This directory contains utility functions specifically designed for YouTube-related operations.
    -   `transcriber.py`: Houses the `get_transcript` function. This function takes a YouTube video URL, extracts its video ID, and uses the `youtube-transcript-api` library to fetch available subtitles or transcripts. It then processes the raw transcript into a dictionary format (`{timestamp_start: 'subtitle text'}`), which is optimized for summarization by the Gemini API.

-   `.gitignore`:
    This file specifies patterns for files and directories that Git should ignore, such as environment variable files (`.env` which contains sensitive API keys) and Python-generated cache directories (`__pycache__/`).