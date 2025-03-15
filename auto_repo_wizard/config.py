import os
from dotenv import load_dotenv

load_dotenv()

# API Key for gemini flash 2.0
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# Path where you want the repo to be cloned
PATH = os.getenv("LOCAL_PATH")
# URL of the repository that you want to clone
URL = os.getenv("REPO_URL")
