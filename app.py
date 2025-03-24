import subprocess
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key as an environment variable
openai.api_key = ""
# Your Mistral API key (provided by you)
MISTRAL_API_KEY = ""

def run_gpt35(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.6,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"GPT-3.5 Error: {e}")
        return None

def run_mistral_cloud(prompt):
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MISTRAL_API_KEY}"
    }
    payload = {
        "model": "mistral-small-latest",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.6,
        "max_tokens": 500,
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Mistral Cloud API Error: {e}")
        return None

def run_mistral_local(prompt):
    ollama_executable = r"C:\Users\shafe\AppData\Local\Programs\Ollama\ollama.exe"
    result = subprocess.run(
        [ollama_executable, "run", "mistral", prompt],
        capture_output=True, text=True, encoding='utf-8', check=True
    )
    return result.stdout.strip()

def run_ai_model(prompt):
    output = run_gpt35(prompt)
    if output:
        print("Used GPT-3.5 successfully.")
        return output
    output = run_mistral_cloud(prompt)
    if output:
        print("Used Mistral Cloud API successfully.")
        return output
    print("Falling back to local Mistral model.")
    return run_mistral_local(prompt)

@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    data = request.get_json()

    keyword_prompt = f"""
    Extract the 15 most important technical and professional keywords from this job description:

    {data['job_description']}

    Keywords (comma-separated):
    """
    keywords_output = run_ai_model(keyword_prompt)
    keywords = [k.strip() for k in keywords_output.split(",")]

    summary_prompt = f"""
    Original professional summary:
    {data['biography']}

    Rewrite this as a concise, single paragraph (max 3-4 sentences), including some keywords: {keywords}. Optimize clearly for ATS.

    Enhanced Professional Summary:
    """
    enhanced_summary = run_ai_model(summary_prompt)

    enhanced_experiences = []
    for exp in data['experiences']:
        exp_prompt = f"""
        Original job description:
        {exp['description']}

        Rewrite strictly as bullet points by including relevant keywords from: {keywords}, add bullet points with keywords if necessary.
        Do NOT alter company names, dates, or roles. ONLY provide bullet points.

        Enhanced bullet points:
        """
        enhanced_text = run_ai_model(exp_prompt)
        enhanced_experiences.append({
            'company': exp['company'],
            'title': exp['title'],
            'duration': f"{exp['start']} - {exp['end']}",
            'description': enhanced_text
        })

    skills_prompt = f"""
    Original skills: {data['skills']}

    Ensure inclusion of relevant keywords from: {keywords}.
    Provide skills comma-separated without additional formatting.

    Enhanced Skills:
    """
    enhanced_skills = run_ai_model(skills_prompt)

    # Certifications explicitly included from input
    certifications = data.get('certifications', '')

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
        resume += f"\n{exp['title']} – {exp['company']} ({exp['duration']}):\n{exp['description'].strip()}\n"

    resume += f"\nEducation:\n{data['school']} – {data['major']}\n"

    # Add Certifications section if provided
    if certifications.strip():
        resume += f"\nCertifications:\n{certifications.strip()}"

    return jsonify({'tailored_resume': resume})


if __name__ == '__main__':
    app.run(debug=True)
