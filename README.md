# YouTube Video Summarizer with Gemini AI

This project provides a robust solution for summarizing YouTube video content by leveraging the powerful Google Gemini AI. It offers two distinct interfaces: a command-line interface (CLI) for quick summarization and a user-friendly Streamlit web application that includes additional features like multi-language translation and summary downloading.

## Features
- **AI-Powered Summarization**: Generates concise summaries of YouTube video transcripts using the Google Gemini API.
- **Transcript Extraction**: Automatically fetches transcripts for YouTube videos using `youtube-transcript-api`.
- **Dual Interfaces**:
    - **Command-Line Interface (CLI)**: For direct, script-based summarization of a given YouTube URL.
    - **Streamlit Web Application**: Provides an interactive graphical user interface (GUI) for a more accessible experience.
- **Multi-Language Translation (Streamlit App)**: Translate the generated summaries into various languages, including Indonesian, English, Japanese, Korean, Spanish, and Arabic.
- **Summary Download (Streamlit App)**: Allows users to download the summarized content as a plain text file directly from the web application.
- **Error Handling**: Includes basic error handling for issues like invalid URLs or failed transcript retrieval.

## Installation

To set up and run this project, follow these steps:

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/galang006/youtube_resume.git
    cd youtube_resume
    ```

2.  **Create a Virtual Environment** (Recommended):
    ```bash
    python -m venv venv
    ```
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Install Dependencies**:
    The project relies on several Python libraries. Install them using pip:
    ```bash
    pip install streamlit google-generativeai python-dotenv youtube-transcript-api yt-dlp
    ```

4.  **Set up Gemini API Key**:
    - Obtain an API key from Google AI Studio ([https://aistudio.google.com/](https://aistudio.google.com/)).
    - Create a file named `.env` in the root directory of your project (where `app.py` and `main.py` are located).
    - Add your Gemini API key to this file in the following format:
        ```
        GEMINI_KEY="YOUR_GEMINI_API_KEY_HERE"
        ```
    - Replace `"YOUR_GEMINI_API_KEY_HERE"` with your actual API key.

## Usage

You can use the project via either the command-line interface or the Streamlit web application.

### Command-Line Interface (CLI)

1.  Ensure your virtual environment is activated.
2.  Run the `main.py` script and follow the prompts:
    ```bash
    python main.py
    ```
3.  Enter the YouTube video URL when prompted.
4.  The summary will be generated and saved as a `.txt` file in the `./resume` directory.

### Streamlit Web Application

1.  Ensure your virtual environment is activated.
2.  Run the `app.py` script using Streamlit:
    ```bash
    streamlit run app.py
    ```
3.  A new tab will open in your web browser displaying the application.
4.  Enter the YouTube video URL into the input field.
5.  (Optional) Select your desired translation language from the dropdown.
6.  Click the "Create a Summary" button.
7.  The summarized and translated content (if applicable) will be displayed on the page. You can also download it using the "Download Ringkasan" button.

## Code Structure

The project is organized into logical directories and files to enhance readability and maintainability:

```
youtube_resume/
├── .gitignore            # Specifies intentionally untracked files to ignore (e.g., .env, __pycache__, resume/)
├── app.py                # Main Streamlit web application for interactive summarization.
├── main.py               # Command-line interface (CLI) script for direct summarization.
├── gemini_api/           # Directory for Gemini API related functionalities.
│   └── client.py         # Handles interaction with the Google Gemini API for generating content.
└── youtube_utils/        # Directory for YouTube utility functions.
    └── transcriber.py    # Contains functions to fetch video titles and transcripts from YouTube.
```

-   **`app.py`**: Orchestrates the Streamlit UI, handles user input, displays results, and integrates with the `gemini_api` and `youtube_utils` modules.
-   **`main.py`**: A simpler script providing a command-line interface for summarization, demonstrating the core functionality without the UI overhead.
-   **`gemini_api/client.py`**: Encapsulates the logic for connecting to the Google Gemini API, sending requests with transcripts and prompts, and receiving AI-generated content. It manages the API key loaded from the `.env` file.
-   **`youtube_utils/transcriber.py`**: Responsible for extracting essential information from YouTube videos, including the video title and the complete transcript, by leveraging `yt-dlp` and `youtube-transcript-api`.