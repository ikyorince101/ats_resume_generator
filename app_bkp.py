import subprocess
from flask import Flask, request, jsonify

from flask_cors import CORS
app = Flask(__name__)
CORS(app)


def run_ai_model(prompt):
    ollama_executable = r"C:\Users\shafe\AppData\Local\Programs\Ollama\ollama.exe"
    result = subprocess.run(
        [ollama_executable, "run", "mistral", prompt],
        capture_output=True, text=True, encoding='utf-8', check=True
    )
    return result.stdout.strip()

@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    data = request.get_json()

    # Extract Keywords from Job Description
    job_description = data['job_description']
    keyword_prompt = f"""
    Extract the 15 most important technical and professional keywords from this job description.

    Job description:
    {job_description}

    Keywords (comma-separated):
    """
    keywords_output = run_ai_model(keyword_prompt)
    keywords = [k.strip() for k in keywords_output.split(",")]

    # Enhance Professional Summary
    summary_prompt = f"""
    Original professional summary:
    {data['biography']}

    Carefully rewrite this summary to include some of these keywords: {keywords}.
    Preserve the general meaning but optimize clearly for ATS.

    Enhanced Professional Summary:
    """
    enhanced_summary = run_ai_model(summary_prompt)

    # Enhance Job Experiences (strictly in bullet points)
    enhanced_experiences = []
    for exp in data['experiences']:
        exp_prompt = f"""
        Original job description:
        {exp['description']}

        Modify and rewrite the above description as clear and concise bullet points (2-4 points). 
        Carefully include relevant keywords from: {keywords}. 
        Do NOT change company names, dates, or introduce new roles. 
        ONLY provide bullet points.

        Enhanced bullet points:
        """
        enhanced_text = run_ai_model(exp_prompt)
        enhanced_experiences.append({
            'company': exp['company'],
            'duration': f"{exp['start']} - {exp['end']}",
            'description': enhanced_text
        })

    # Enhance Skills (you were satisfied with this, but explicitly ensure it again)
    skills_prompt = f"""
    Original skills: {data['skills']}

    Ensure inclusion of relevant keywords from: {keywords}.
    Provide skills comma-separated without additional formatting or text.

    Enhanced Skills:
    """
    enhanced_skills = run_ai_model(skills_prompt)

    # Stitch the final Resume
    resume = f"""
{data['name']}
{data['phone']} | {data['city']}, {data['state']}

Professional Summary:
{enhanced_summary.strip()}

Skills:
{enhanced_skills.strip()}

Work Experience:
"""

    for exp in enhanced_experiences:
        resume += f"\n{exp['company']} ({exp['duration']}):\n{exp['description'].strip()}\n"

    resume += f"\nEducation:\n{data['school']} – {data['major']}"

    return jsonify({'tailored_resume': resume})


if __name__ == '__main__':
    app.run(debug=True)
