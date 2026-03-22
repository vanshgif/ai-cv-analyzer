

def detect_role(text):
    text = text.lower()

    if "data scientist" in text or "machine learning" in text:
        return "data_scientist"
    elif "frontend" in text or "react" in text:
        return "frontend"
    elif "backend" in text or "django" in text:
        return "backend"
    else:
        return "general"

# Predefined skill list (we expand later)
SKILLS_DB = [
    "python", "django", "flask", "react", "node", "javascript",
    "machine learning", "deep learning", "nlp", "sql", "mongodb",
    "pandas", "numpy", "tensorflow", "pytorch", "aws", "docker"
]

ROLE_SKILLS = {
    "backend": ["python", "django", "api", "sql", "docker"],
    "frontend": ["react", "javascript", "html", "css"],
    "data_scientist": ["python", "pandas", "numpy", "machine learning"],
    "general": ["communication", "teamwork"]
}

def extract_skills(text):
    role = detect_role(text)
    skills_db = ROLE_SKILLS.get(role, [])

    found_skills = []

    for skill in skills_db:
        if skill in text.lower():
            found_skills.append(skill.title())

    return list(set(found_skills)), role