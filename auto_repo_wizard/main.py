import os
from auto_repo_wizard.repo_manager import clone_repo
from auto_repo_wizard.file_manager import get_all_files
from auto_repo_wizard.llm import explain_code
from auto_repo_wizard.config import PATH, URL



if __name__ == "__main__":
    print("--Cloning the repo")
    clone_repo(PATH, URL)
    print("--Repo Cloned")
    print("--Extract all file names with .py")
    python_files = get_all_files(PATH)
    print("--Files Extracted")
    print("--Generating explanation")
    explain_code(python_files)
    print("--Generated Explanations and stored")
