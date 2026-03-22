from .nlp import ROLE_SKILLS

def calculate_score(skills, text, role):
    score = 0
    breakdown = {}

    expected = ROLE_SKILLS.get(role, [])
    matched = len(set([s.lower() for s in skills]) & set(expected))

    # Skill score (dynamic)
    skill_score = int((matched / len(expected)) * 40) if expected else 0
    breakdown["skills"] = skill_score
    score += skill_score

    # Experience score
    exp_score = 20 if "year" in text.lower() else 0
    breakdown["experience"] = exp_score
    score += exp_score

    # Keyword score
    keywords = ["developed", "built", "designed"]
    keyword_score = sum([5 for k in keywords if k in text.lower()])
    keyword_score = min(keyword_score, 15)
    breakdown["keywords"] = keyword_score
    score += keyword_score

    # Projects
    project_score = 15 if "project" in text.lower() else 0
    breakdown["projects"] = project_score
    score += project_score

    # Certifications
    cert_score = 10 if "certificate" in text.lower() else 0
    breakdown["certifications"] = cert_score
    score += cert_score

    return {
        "total_score": score,
        "breakdown": breakdown
    }