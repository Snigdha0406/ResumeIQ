import re

def clean_text(text):
    """
    Clean extracted resume text while preserving line breaks.
    """

    # Replace multiple spaces/tabs with a single space
    text = re.sub(r"[ \t]+", " ", text)

    # Remove spaces around newlines
    text = re.sub(r" *\n *", "\n", text)

    # Replace 3 or more newlines with 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove leading/trailing whitespace
    text = text.strip()

    return text