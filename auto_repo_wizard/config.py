# Import the os module for interacting with the operating system.
import os
# Import the load_dotenv function from the dotenv module to load environment variables from a .env file.
from dotenv import load_dotenv

# Load environment variables from a .env file into the environment.
load_dotenv()

# Retrieve the value of the environment variable "GEMINI_API_KEY" and assign it to the GEMINI_API_KEY variable.
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# Retrieve the value of the environment variable "LOCAL_PATH" and assign it to the PATH variable.
PATH = os.getenv("LOCAL_PATH")
# Retrieve the value of the environment variable "REPO_URL" and assign it to the URL variable.
URL = os.getenv("REPO_URL")