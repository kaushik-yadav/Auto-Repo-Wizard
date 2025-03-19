from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from fastapi.middleware.cors import CORSMiddleware
# If you need to import local modules
from .repo_manager import clone_repo
from .file_manager import get_all_files
from .llm import explain_code

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development, "*" allows all origins. For production, list allowed origins.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model to define the body of our POST request
class CloneRequest(BaseModel):
    url: str       # GitHub repo URL
    path: str      # Destination path
    explain: bool  # True if user wants code explanation

@app.post("/clone")
def clone_repository(request: CloneRequest):
    """
    1. Clones the repo from request.url into request.path
    2. If request.explain is True, it runs explain_code on the cloned files.
    """

    # 1) Validate input
    if not request.url:
        raise HTTPException(status_code=400, detail="Repository URL is required.")
    if not request.path:
        raise HTTPException(status_code=400, detail="Destination path is required.")

    # 2) Clone the repository
    try:
        clone_repo(request.path, request.url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error cloning repository: {str(e)}")

    # 3) If explanation is requested, run the llm.explain_code
    if request.explain:
        # Collect all .py files in the newly cloned repo
        python_files = get_all_files(request.path)
        if python_files:
            try:
                explain_code(python_files)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error explaining code: {str(e)}")

    return {"status": "success", "explanation": request.explain}
