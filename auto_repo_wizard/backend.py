# Import the FastAPI class and the HTTPException class from the fastapi library.
from fastapi import FastAPI, HTTPException
# Import the BaseModel class from the pydantic library.
from pydantic import BaseModel
# Import the os module for interacting with the operating system.
import os
# Import the CORSMiddleware class from the fastapi.middleware.cors module.
from fastapi.middleware.cors import CORSMiddleware
# Import the clone_repo function from the local repo_manager module.
from .repo_manager import clone_repo
# Import the get_all_files function from the local file_manager module.
from .file_manager import get_all_files
# Import the explain_code function from the local llm module.
from .llm import explain_code


# Create an instance of the FastAPI class.
app = FastAPI()

# Add CORS middleware to the FastAPI application.
# Ensure the middleware is properly configured
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

# Define a Pydantic model named CloneRequest, inheriting from BaseModel.
class CloneRequest(BaseModel):
    # Define a field named 'url' of type string to store the GitHub repo URL.
    url: str       # GitHub repo URL
    # Define a field named 'path' of type string to store the destination path.
    path: str      # Destination path
    # Define a field named 'explain' of type boolean to indicate whether code explanation is requested.
    explain: bool  # True if user wants code explanation

# Define a POST endpoint at "/clone" using the @app.post decorator.
@app.post("/clone")
# Define a function named clone_repository that takes a CloneRequest object as input.
def clone_repository(request: CloneRequest):
    """
    1. Clones the repo from request.url into request.path
    2. If request.explain is True, it runs explain_code on the cloned files.
    """

    # Validate that the repository URL is not empty.
    if not request.url:
        # Raise an HTTPException with a 400 status code (Bad Request) if the URL is missing.
        raise HTTPException(status_code=400, detail="Repository URL is required.")
    # Validate that the destination path is not empty.
    if not request.path:
        # Raise an HTTPException with a 400 status code (Bad Request) if the path is missing.
        raise HTTPException(status_code=400, detail="Destination path is required.")

    # Attempt to clone the repository using the clone_repo function.
    try:
        # Call the clone_repo function with the destination path and repository URL from the request.
        clone_repo(request.path, request.url)
    # Catch any exceptions that occur during the cloning process.
    except Exception as e:
        # Raise an HTTPException with a 500 status code (Internal Server Error) if an error occurs.
        raise HTTPException(status_code=500, detail=f"Error cloning repository: {str(e)}")

    # Check if the user requested code explanation.
    if request.explain:
        # Collect all .py files in the newly cloned repo
        python_files = get_all_files(request.path)
        # Check if any Python files were found.
        if python_files:
            # Attempt to explain the code in the Python files using the explain_code function.
            try:
                # Call the explain_code function with the list of Python files.
                explain_code(python_files)
            # Catch any exceptions that occur during the code explanation process.
            except Exception as e:
                # Raise an HTTPException with a 500 status code (Internal Server Error) if an error occurs.
                raise HTTPException(status_code=500, detail=f"Error explaining code: {str(e)}")

    # Return a dictionary indicating the status of the operation and whether explanation was requested.
    return {"status": "success", "explanation": request.explain}