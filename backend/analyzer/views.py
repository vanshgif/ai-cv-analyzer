from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.parser import extract_text_from_pdf
from .utils.nlp import extract_skills
from .utils.scoring import calculate_score
from .utils.recommendations import generate_recommendations
from .utils.github import fetch_github_data
from .utils.llm import generate_llm_feedback

@api_view(['POST'])
def upload_cv(request):
    file = request.FILES.get('file')
    github_username = request.data.get('github')

    if not file:
        return Response({"error": "No file uploaded"}, status=400)

    text = extract_text_from_pdf(file)
    skills, role = extract_skills(text)
    score_data = calculate_score(skills, text, role)

    llm_feedback = generate_llm_feedback(
    text,
    skills,
    score_data["total_score"],
    role
)

    recommendations = generate_recommendations(
        skills,
        text,
        score_data["total_score"],
        role
    
    
    )

    github_data = None
    if github_username:
        github_data = fetch_github_data(github_username)
    print("GitHub data:", github_data)
    print("GitHub username:", github_username)
    return Response({
        "skills": skills,
        "role": role,
        "score": score_data["total_score"],
        "breakdown": score_data["breakdown"],
        "recommendations": recommendations,
        "github": github_data,
        "llm_feedback": llm_feedback
    })