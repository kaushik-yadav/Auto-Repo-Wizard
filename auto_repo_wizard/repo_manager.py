# Imports the os module for interacting with the operating system
import os
# Imports the shutil module for high-level file operations
import shutil
# Imports the subprocess module to run external commands
import subprocess


# Defines a function to remove read-only permissions from a file, allowing deletion
def remove_readonly(func, path, _):
    # Changes the file permissions to allow writing (0o777 is octal for rwxrwxrwx)
    os.chmod(path, 0o777)
    # Executes the provided function (e.g., os.remove or shutil.rmtree) on the given path
    func(path)


# Defines a function to clone a Git repository and install its dependencies
def clone_repo(path, url):
    # Extracts the file name from the URL
    try:
        # Splits the URL by "/", takes the last part, splits by ".", and takes the first part to get the file name
        file_name = url.split("/")[-1].split(".")[0]
    # Handles exceptions that might occur during URL parsing
    except Exception:
        # Prints an error message if the URL is incorrect
        print("-- Provide correct url")
        # Exits the function
        return

    # Checks if the specified path exists
    if not os.path.exists(path):
        # Prints an error message if the path does not exist
        print(f"-- Error: Path '{path}' does not exist")
        # Exits the function
        return

    # Changes the current working directory to the specified path
    os.chdir(path)

    # Checks if a directory with the extracted file name already exists
    if os.path.exists(file_name):
        # Prints a message indicating that the existing repository folder will be removed
        print("-- Removing existing repository folder as it already exists")
        # Removes the existing directory recursively, using the remove_readonly function to handle read-only files
        shutil.rmtree(file_name, onerror=remove_readonly)

    # Clones the Git repository from the provided URL using the git clone command
    subprocess.run(f"git clone {url}", shell=True, check=True)

    # Changes the current working directory to the newly cloned repository folder
    os.chdir(file_name)

    # Creates a virtual environment named "venv" in the current directory
    subprocess.run("python -m venv venv", shell=True, check=True)

    # Checks if a requirements.txt file exists in the current directory
    if "requirements.txt" in os.listdir():
        # Installs the dependencies listed in the requirements.txt file using pip
        subprocess.run(
            "venv\\Scripts\\python -m pip install -r requirements.txt",
            shell=True,
            check=True,
        )
    # If requirements.txt does not exists
    else:
        # Prints a message indicating that the requirements file does not exist
        print("-- Requirements file does not exist")
        