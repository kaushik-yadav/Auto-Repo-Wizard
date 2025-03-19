# Imports the os module for interacting with the operating system.
import os

# Defines a function to get all Python files in a directory, excluding specified directories.
def get_all_files(directory_path):
    # Defines a list of directories to exclude from the search.
    exclude_dirs = ["venv", ".git", "__pycache__"]
    # Initializes an empty list to store the paths of Python files.
    python_files = []
    # Walks through the directory tree starting from the given directory path.
    for root, dirs, files in os.walk(directory_path):
        # Modifies the 'dirs' list in-place to exclude directories in the 'exclude_dirs' list.
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        # Iterates through the files in the current directory.
        for file in files:
            # Checks if the file ends with ".py", indicating it's a Python file.
            if file.endswith(".py"):
                # Constructs the full path to the file by joining the root directory and the file name.
                full_path = os.path.join(root, file)
                # Appends the full path to the list of Python files.
                python_files.append(full_path)
    # Returns the list of Python file paths.
    return python_files

# Defines a function to read the content of a file.
def read_file_content(file):
    # Opens the file in read mode with UTF-8 encoding, ensuring proper character handling.
    with open(file, "r", encoding="utf-8") as file:
        # Reads the entire content of the file into a string.
        content = file.read()
        # Returns the content of the file.
        return content

# Defines a function to clean a response and write it to a file.
def write_clean_response(file_path, response):
    # Strips leading/trailing whitespaces from the response text and splits it into a list of lines.
    response_lines = response.text.strip().split("\n")

    # Removes the first and last lines from the list of lines.
    cleaned_response = "\n".join(response_lines[1:-1])
    # Opens the file in write mode with UTF-8 encoding.
    with open(file_path, "w", encoding="utf-8") as file:
        # Writes the cleaned response to the file.
        file.write(cleaned_response)