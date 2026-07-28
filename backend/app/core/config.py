import os

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Gemini API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY is missing. Please add it to your .env file."
    )