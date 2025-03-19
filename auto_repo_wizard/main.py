# Imports the 'os' module, which provides functions for interacting with the operating system.
import os
# Imports the 'clone_repo' function from the 'auto_repo_wizard.repo_manager' module.
from auto_repo_wizard.repo_manager import clone_repo
# Imports the 'get_all_files' function from the 'auto_repo_wizard.file_manager' module.
from auto_repo_wizard.file_manager import get_all_files
# Imports the 'explain_code' function from the 'auto_repo_wizard.llm' module.
from auto_repo_wizard.llm import explain_code
# Imports the 'PATH' and 'URL' variables from the 'auto_repo_wizard.config' module.
from auto_repo_wizard.config import PATH, URL

# Checks if the script is being run as the main program.
if __name__ == "__main__":
    # Prints a message indicating that the repository is being cloned.
    print("--Cloning the repo")
    # Clones the repository from the specified URL to the specified path.
    clone_repo(PATH, URL)
    # Prints a message indicating that the repository has been cloned.
    print("--Repo Cloned")
    # Prints a message indicating that the script is extracting all file names with .py extension.
    print("--Extract all file names with .py")
    # Calls the 'get_all_files' function to get a list of all Python files in the specified path.
    python_files = get_all_files(PATH)
    # Prints a message indicating that the files have been extracted.
    print("--Files Extracted")
    # Prints a message indicating that the script is generating explanations for the code.
    print("--Generating explanation")
    # Calls the 'explain_code' function to generate explanations for the code in the extracted Python files.
    explain_code(python_files)
    # Prints a message indicating that the explanations have been generated and stored.
    print("--Generated Explanations and stored")