import warnings

warnings.filterwarnings("ignore", message="Field name .* shadows an attribute in parent .*")

from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

def generate_content(contents, model = "gemini-2.5-flash"):
    """
    Generate content using the specified model and contents.
    :param model: The model to use for content generation.
    :param contents: The input contents for the model.
    :return: The generated content response.
    """
    client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

    response = client.models.generate_content(
        model=model, contents=contents,
    )
    
    return response.text