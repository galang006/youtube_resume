import warnings

warnings.filterwarnings("ignore", message="Field name .* shadows an attribute in parent .*")

from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Can you write resume from youtube transcript?",
)
print(response.text)