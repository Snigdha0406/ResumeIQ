from fastapi import APIRouter, UploadFile, File
from app.services.resume_parser import extract_resume_text
from app.utils.text_cleaner import clean_text
import os
import shutil

router = APIRouter()

# Folder where uploaded resumes will be stored
UPLOAD_FOLDER = "uploads"

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    # Allow only PDF and DOCX files
    if not file.filename.endswith((".pdf", ".docx")):
        return {
            "error": "Only PDF and DOCX files are allowed."
        }

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_resume_text(file_path)
    text=clean_text(text)
    print(text)
    return {
        "message": "Resume uploaded successfully!",
        "filename": file.filename,
        "extracted_text": text
}