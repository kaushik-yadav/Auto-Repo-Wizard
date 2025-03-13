import os
import shutil
import subprocess

# Hardcoded the values for now
PATH = "C:\\Users\\Anuj\\Desktop\\test"
URL = "https://github.com/kaushik-yadav/VisaFriendly_assignment.git"


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


if __name__ == "__main__":
    clone_repo(PATH, URL)
