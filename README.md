# Auto-Repo-Wizard

## Overview
Auto-Repo-Wizard is a Python-based tool that automates the process of cloning a GitHub repository, setting up a virtual environment, installing dependencies, and generating inline code explanations using Google's Gemini API.

## Features
- Clone a GitHub repository automatically.
- Set up a virtual environment and install dependencies.
- Extract all Python files from the repository.
- Use Google's Gemini API to generate inline comments explaining each line of code.
- Overwrite the original files with commented versions.

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/YOUR_GITHUB_USERNAME/Auto-Repo-Wizard.git
   cd Auto-Repo-Wizard
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration
1. Set up your environment variables in a `.env` file inside the project root:
   ```ini
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
   You can obtain an API key from [Google AI Studio](https://aistudio.google.com/) after signing in.

2. Update the `main.py` file with your desired repository URL and local path:
   ```python
   PATH = "YOUR_LOCAL_DIRECTORY"
   URL = "YOUR_GITHUB_REPOSITORY_URL"
   ```

## Usage
Run the script to automate the cloning and code explanation process:
```sh
python -m auto_repo_wizard.main
```

The tool will:
1. Clone the specified repository.
2. Identify all `.py` files.
3. Generate and overwrite the files with explanations.
4. Print progress messages.

## File Structure
```
Auto-Repo-Wizard/
│── auto_repo_wizard/
│   │── __init__.py
│   │── main.py
│   │── llm.py
│   │── utils.py
│── .env
│── .gitignore
│── requirements.txt
│── README.md
```

## License
This project is licensed under the MIT License. Feel free to contribute!

