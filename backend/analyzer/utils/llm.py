import google.generativeai as genai
import os
import dotenv

dotenv.load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-3-flash-preview")

def generate_llm_feedback(text, skills, score, role):
    prompt = f"""
You are an AI career coach.

Analyze this CV:

{text[:2000]}

Detected Role: {role}
Skills: {skills}
Score: {score}/100

Give:
1. Strengths
2. Weaknesses
3. Specific improvements
4. Career advice

Be concise and structured.
"""

    response = model.generate_content(prompt)

    return response.text