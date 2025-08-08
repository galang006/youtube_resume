# YouTube Transcript Summarizer using Gemini API

This project leverages the Gemini API to generate summaries of YouTube video transcripts. It fetches the transcript of a YouTube video using a YouTube transcription library and then passes it to the Gemini API for content generation.  The generated summary is then printed to the console.


## Features

- Fetches YouTube video transcripts.
- Uses the Gemini API to generate a summary of the transcript.
- Prints the generated summary to the console.


## Prerequisites

- **Python 3.7 or higher:** The code is written in Python and requires at least version 3.7.
- **gemini-api:** This library provides the interface to the Gemini API. Install using pip.
- **youtube_utils:** A library for fetching YouTube video transcripts.  You'll need to install this library.  The specific library used is not defined within the provided code.
- **A valid Gemini API key:**  This is crucial for interacting with the Gemini API and generating summaries. The key is typically set as an environment variable.


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/galang006/youtube_resume
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   ```
   gemini-api
   youtube_utils
   ```

4. **Set up your environment variables:**

   Create a `.env` file in the project's root directory and add your Gemini API key:

   ```
   GEMINI_API_KEY=your_gemini_api_key
   ```
   **Important:**  `.env` is added to `.gitignore` to prevent accidental commits of your API key.  Make sure the `.env` file is not checked into version control.


## Usage

1. **Activate your virtual environment:**

   ```bash
   source .venv/bin/activate  
   ```

2. **Run the script:**

   ```bash
   python main.py
   ```

   This will fetch the transcript from the specified YouTube video URL and print the Gemini API-generated summary to your console.  Modify the `video_url` variable in `main.py` to process a different video.


## Code Structure

- **`main.py`:** This file contains the main logic of the program. It fetches the transcript, calls the Gemini API for content generation, and prints the results.
- **`.gitignore`:** This file specifies files and directories to exclude from version control, notably `.env` to protect the API key.
- **`gemini_api/`:**  This directory likely contains the `gemini_api.client` module which is responsible for communication with the Gemini 
API.
- **`youtube_utils/`:** This directory likely contains the `youtube_utils.transcriber` module which handles fetching YouTube video transcripts.



**Note:**  This documentation assumes the existence of `gemini_api` and `youtube_utils` libraries.  You will need to obtain and install these appropriately to 
run this code.  The provided code snippet doesn't include the implementation details of these libraries.  Error handling (e.g., for API request failures or network issues) would be a necessary addition for a robust application.