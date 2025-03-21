import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .file_manager import get_all_files
from .llm import explain_code
from .repo_manager import clone_repo

# Create an instance of the FastAPI class.
app = FastAPI()

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
    url: str
    path: str
    explain: bool


@app.post("/clone")
def clone_repository(request: CloneRequest):
    """Clones the repo and if user asked for explanation then generate the explanations for each code file"""

    # Validate that the repository URL is not empty.
    if not request.url:
        raise HTTPException(status_code=400, detail="Repository URL is required.")
    if not request.path:
        raise HTTPException(status_code=400, detail="Destination path is required.")

    try:
        # Call the clone_repo function with the destination path and repository URL from the request.
        clone_repo(request.path, request.url)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error cloning repository: {str(e)}"
        )

    # If user requested for explanation
    if request.explain:
        # Collect all .py files in the newly cloned repo
        python_files = get_all_files(request.path)
        if python_files:
            # If python files exist then try our explanation block
            try:
                # Call the explain_code function with the list of Python files.
                explain_code(python_files)
            except Exception as e:
                raise HTTPException(
                    status_code=500, detail=f"Error explaining code: {str(e)}"
                )

    return {"status": "success", "explanation": request.explain}
