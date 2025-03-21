import os

from dotenv import load_dotenv

# Load environment variables from a .env file into the environment.
load_dotenv()

# Setting the env variables so that other files can easily import them
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PATH = os.getenv("LOCAL_PATH")
URL = os.getenv("REPO_URL")
