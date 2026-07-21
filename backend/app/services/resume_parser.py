from pypdf import PdfReader
from docx import Document

def extract_pdf_text(file_path):
    """
    Extract text from a PDF resume.
    """

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text
def extract_docx_text(file_path):
    """
    Extract text from a DOCX resume.
    """

    document = Document(file_path)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text
def extract_resume_text(file_path):
    """
    Detect the file type and extract text.
    """

    if file_path.endswith(".pdf"):
        return extract_pdf_text(file_path)

    elif file_path.endswith(".docx"):
        return extract_docx_text(file_path)

    else:
        return "Unsupported file format."