
# Auto-Repo-Wizard

## Overview
Auto-Repo-Wizard is a comprehensive tool designed to automate cloning a GitHub repository, setting up a Python virtual environment, installing dependencies, and enhancing your code with inline explanations powered by Google's Gemini API. In this update, we've added a browser extension—now located in its own dedicated folder—to inject a "Clone" button directly onto GitHub repository pages for a seamless cloning experience.

## Features
- **Automated Repository Cloning**: Clone a GitHub repository to a specified local path.
- **Environment Setup**: Automatically create a virtual environment and install dependencies (if a `requirements.txt` is present).
- **Inline Code Explanation**: Use Google's Gemini API to generate inline comments for Python files.
- **Browser Extension Integration**: A new browser extension (found in the `extension` folder) adds a convenient "Clone" button to GitHub pages.
- **Centralized Configuration**: All sensitive settings, including your Gemini API key, are managed in the `.env` file.

## Installation and Setup

### Backend Setup
1. **Clone the Repository:**
   
   git clone https://github.com/YOUR_GITHUB_USERNAME/Auto-Repo-Wizard.git
   cd Auto-Repo-Wizard

2. **Create and Activate a Virtual Environment:**
   
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate

3. **Install Dependencies:**
   pip install -r requirements.txt


4. **Configuration:**
   - Create a `.env` file in the project root with the following content:
    
     GEMINI_API_KEY=your_gemini_api_key_here
     LOCAL_PATH=your_local_destination_path
     REPO_URL=your_default_repository_url

     You can obtain an API key from Google AI Studio after signing in.
    
   - Replace the placeholders with your actual API key and paths. (See [config.py] for how these values are used.)

5. **Run the Backend Service:**
   ```sh
   uvicorn auto_repo_wizard.backend:app --reload
   ```
   This command starts the FastAPI server that handles cloning and code explanation requests.

### Browser Extension Setup
The project now includes a browser extension to streamline repository cloning from GitHub.

1. **Load the Extension:**
   - Open your Chromium-based browser (Chrome, Edge, etc.).
   - Navigate to the extensions management page (e.g., `chrome://extensions/`).
   - Enable **Developer Mode**.
   - Click **Load unpacked** and select the `extension` folder from the project directory.

2. **Usage:**
   - When browsing any GitHub repository, a "Clone" button will appear (see [content.js] and [manifest.json] for details).
   - Click the button to open a dialog where you can specify your destination path and choose whether to generate inline code explanations.
   - The extension will then send a POST request to the backend, triggering the cloning and explanation processes.

3. **Unloading/Removing the Extension:**
   - To disable or remove the extension, simply return to your browser’s extension management page (e.g., `chrome://extensions/`) and click **Remove** or toggle it off.

## File Structure
```
Auto-Repo-Wizard/
├── auto_repo_wizard/
│   ├── backend.py
│   ├── config.py
│   ├── file_manager.py
│   ├── llm.py
│   ├── main.py
│   └── repo_manager.py
├── extension/
│   ├── content.js
│   └── manifest.json
├── .env
├── README.md
├── requirements.txt

```
*Note: The `extension` folder contains all files related to the browser extension integration.*

## Updated Components
- **Extension Integration**: The new extension (located in the `extension` folder) now adds a "Clone" button on GitHub pages for direct repository cloning.
- **Configuration Management**: The `.env` file now manages critical settings like the `GEMINI_API_KEY`, ensuring a more secure and streamlined setup.
- **Enhanced Code Explanation**: Inline code comments are now generated more efficiently using Google's Gemini API, as detailed in [llm.py].

## Usage Workflow
1. **Backend Operation**:
   - Clones the repository.
   - Sets up the virtual environment and installs dependencies.
   - Scans for Python files and applies inline code explanations.
2. **Extension Operation**:
   - Injects a "Clone" button on GitHub repository pages.
   - Allows users to specify cloning options via a simple dialog.
   - Triggers backend operations based on user selections.

## License
This project is licensed under the MIT License. Contributions are welcome—please feel free to submit issues or pull requests on [GitHub](https://github.com/YOUR_GITHUB_USERNAME/Auto-Repo-Wizard).


README should help users understand both the backend and the newly integrated extension components, as well as guide them through installation, usage, and extension management. Enjoy using Auto-Repo-Wizard!