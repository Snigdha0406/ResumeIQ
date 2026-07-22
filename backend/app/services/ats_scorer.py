def calculate_ats_score(text):
    """
    Calculates ATS score and returns score breakdown.
    """

    text = text.lower()

    breakdown = {
        "contact_details": 0,
        "education": 0,
        "skills": 0,
        "projects": 0,
        "experience": 0,
        "certifications": 0,
        "achievements": 0,
        "structure": 0
    }

    # Contact Details
    if "@" in text:
        breakdown["contact_details"] = 10

    # Education
    if "education" in text:
        breakdown["education"] = 10

    # Skills
    if "skills" in text:
        breakdown["skills"] = 20

    # Projects
    if "project" in text:
        breakdown["projects"] = 20

    # Experience / Internship
    if "experience" in text or "internship" in text:
        breakdown["experience"] = 15

    # Certifications
    if "certification" in text or "certifications" in text:
        breakdown["certifications"] = 10

    # Achievements
    if "achievement" in text or "achievements" in text:
        breakdown["achievements"] = 5

    # Structure
    headings = [
        "career objective",
        "education",
        "skills",
        "experience",
        "projects",
        "strengths"
    ]

    count = sum(1 for heading in headings if heading in text)

    if count >= 4:
        breakdown["structure"] = 10

    total_score = sum(breakdown.values())

    return {
        "ats_score": min(total_score, 100),
        "score_breakdown": breakdown
    }