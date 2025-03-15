import os
from google import genai
from dotenv import load_dotenv
from utils import get_file_content
from utils import write_clean_response

load_dotenv()

gemini_api = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=gemini_api)


def explain_code(python_files):

    for file_path in python_files:
        content = get_file_content(file_path)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"""Rewrite the following Python code so that each line is preceded by an inline comment 
        (that should be on top of the code line) that explains only that line. 
        Do not add any extra code, functions, or examples. Only comment the given code. 
        If a comment already exists but is not descriptive enough, then make it better.

        Code:
        {content}
        """,
        )
        # Writes the explained code with comments in the file(overwriiten)
        write_clean_response(file_path, response)
    print(response.text)
