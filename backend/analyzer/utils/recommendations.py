from .nlp import ROLE_SKILLS

def generate_recommendations(skills, text, score, role):
    recommendations = []

    expected = ROLE_SKILLS.get(role, [])
    current = [s.lower() for s in skills]

    missing = [skill for skill in expected if skill not in current]

    if missing:
        recommendations.append(f"Focus on learning: {', '.join(missing)}")

    if score < 70:
        recommendations.append("Improve your resume with stronger projects")

    if "project" not in text.lower():
        recommendations.append("Add real-world projects to your CV")

    if "developed" not in text.lower():
        recommendations.append("Use action words like Developed, Built, Designed")

    return recommendations