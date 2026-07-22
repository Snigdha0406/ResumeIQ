from groq import Groq
from dotenv import load_dotenv
import os
import json
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_resume(text):
    """
    Analyze resume using Groq AI.
    """

    prompt = f"""
Analyze the following resume.

Resume:
{text}

Return ONLY valid JSON.

The JSON must have exactly these fields:

{{
  "ats_score": number,
  "skills": [],
  "strengths": [],
  "missing_skills": [],
  "suggestions": []
}}

Rules:
- ats_score must be an integer between 0 and 100.
- skills must contain only technical skills found in the resume.
- strengths must be an array of short points.
- missing_skills must contain important technical skills that would improve the resume.
- suggestions must contain concise improvement suggestions.
- Do not include markdown.
- Do not include explanations.
- Do not write anything outside the JSON.
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    result = response.choices[0].message.content

    return json.loads(result)