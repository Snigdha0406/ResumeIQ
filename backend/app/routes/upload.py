from fastapi import APIRouter, UploadFile, File
from app.services.resume_parser import extract_resume_text
from app.services.resume_analyzer import analyze_resume
from app.services.ats_scorer import calculate_ats_score
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
    ats_result=calculate_ats_score(text)
    analysis=analyze_resume(text)
    analysis["ats_score"]=ats_result["ats_score"]
    analysis["score_breakdown"]=ats_result["score_breakdown"]
    print(text)
    return {
    "message": "Resume uploaded successfully!",
    "filename": file.filename,
    "extracted_text": text,
    "analysis": analysis
}