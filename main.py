from utils import clone_repo, get_all_files, get_file_content, write_clean_response
from llm import explain_code

# Hardcoded the values for now
PATH = "C:\\Users\\Anuj\\Desktop\\test"
URL = "https://github.com/kaushik-yadav/VisaFriendly_assignment.git"


if __name__ == "__main__":
    print("--cloning the repo")
    clone_repo(PATH, URL)
    print("--cloned the repo")
    print("--Extract all file names with .py")
    python_files = get_all_files(PATH)
    print("--got all the files")
    print("--Generating explanation")
    explain_code(python_files)
    print("--generated and stored")
