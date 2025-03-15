import os
import shutil
import subprocess


# Change permissions to allow deletion
def remove_readonly(func, path, _):
    os.chmod(path, 0o777)
    func(path)


# Function to clone the repo and install dependencies if found
def clone_repo(path, url):
    # Extract file name from the url
    try:
        file_name = url.split("/")[-1].split(".")[0]
    except Exception:
        print("-- Provide correct url")
        return

    # Check if directory exists else exit
    if not os.path.exists(path):
        print(f"-- Error: Path '{path}' does not exist")
        return

    # Change to the main directory
    os.chdir(path)

    # Delete existing folder if it exists
    if os.path.exists(file_name):
        print("-- Removing existing repository folder as it already exists")
        shutil.rmtree(file_name, onerror=remove_readonly)

    # Clone the repo
    subprocess.run(f"git clone {url}", shell=True, check=True)

    # Change directory to new file location
    os.chdir(file_name)

    # Create a virtual environment
    subprocess.run("python -m venv venv", shell=True, check=True)

    # Install dependencies if requirements.txt exists otherwise print that it doesnt exist
    if "requirements.txt" in os.listdir():
        subprocess.run(
            "venv\\Scripts\\python -m pip install -r requirements.txt",
            shell=True,
            check=True,
        )
    else:
        print("-- Requirements file does not exist")


def get_all_files(directory_path):
    exclude = ["venv", ".git", "__pycache__"]
    python_files = []
    for root, dirs, files in os.walk(directory_path):
        # Modfies the list in place and excludes .py files from the exclude list
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                python_files.append(full_path)
    return python_files


def get_file_content(file):
    with open(file, "r", encoding="utf-8") as file:
        content = file.read()
        return content


def write_clean_response(file_path, response):
    response_lines = response.text.strip().split("\n")

    # Remove the first and last lines
    cleaned_response = "\n".join(response_lines[1:-1])
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(cleaned_response)
