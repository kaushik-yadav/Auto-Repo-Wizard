from google import genai

from .config import GEMINI_API_KEY
from .file_manager import read_file_content, write_clean_response

client = genai.Client(api_key=GEMINI_API_KEY)


# Generates explanation(inline comments) for all code files in a directory
def explain_code(python_files):
    for file_path in python_files:
        content = read_file_content(file_path)

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"""
            Rewrite the following Python code so that each line is preceded by an inline comment 
            (that should be on top of the code line) that explains only that line. 
            Do not add any extra code, functions, or examples. Only comment the given code. 
            If a comment already exists but is not descriptive enough, then make it better.

            Code:
            {content}
            """,
        )

        # writes the cleaned response in a file
        write_clean_response(file_path, response)

    print("-- Code explanation process completed")
