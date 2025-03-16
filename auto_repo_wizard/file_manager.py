import os


# Fetch all the files present in the directory with extension .py
# Except for files in exclude directories
def get_all_files(directory_path):
    exclude_dirs = ["venv", ".git", "__pycache__"]
    python_files = []
    for root, dirs, files in os.walk(directory_path):
        # Modfies the list in place and excludes .py files from the exclude list
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                python_files.append(full_path)
    return python_files
#gay ass niggers

# Opens the file and returns the content inside
def read_file_content(file):
    with open(file, "r", encoding="utf-8") as file:
        content = file.read()
        return content


# Cleans the response and writes it in the same file
def write_clean_response(file_path, response):
    # strips whitespaces and splits on basis on lines (so it would be easy to remove first and last line)
    response_lines = response.text.strip().split("\n")

    # Remove the first and last line
    cleaned_response = "\n".join(response_lines[1:-1])
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(cleaned_response)
