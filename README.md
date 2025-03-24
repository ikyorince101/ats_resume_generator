# AI Resume Tailoring Application

An AI-powered application that tailors your resume specifically for job descriptions, optimizing for ATS (Applicant Tracking Systems) and highlighting relevant keywords and experiences to increase your chances of getting shortlisted.

## 🚀 Features
- **AI-powered keyword extraction** from job descriptions.
- **Automatic tailoring** of Professional Summary, Skills, and Job Experiences.
- **Multiple AI model support:** GPT-3.5, Mistral Cloud API, and local Mistral as fallback.
- **Real-time generation** with clear comparison between original and tailored resumes.
- **User-friendly** frontend using plain HTML, CSS, and JavaScript.

## 🔧 Tech Stack

### Backend
- Python
- Flask
- OpenAI GPT-3.5 API
- Mistral API
- Ollama for local model inference

### Frontend
- HTML
- CSS
- Vanilla JavaScript

## 📌 Setup Instructions

### Backend Setup

1. **Clone Repository**
```bash
git clone https://github.com/yourusername/ai-resume-generator.git
cd ai-resume-generator
```

2. **Install Dependencies**
```bash
pip install flask flask-cors openai requests
```

3. **Configure API keys**

Set environment variables for your APIs:
```bash
export OPENAI_API_KEY="your-openai-api-key"
export MISTRAL_API_KEY="your-mistral-api-key"
```

4. **Run Backend**
```bash
python app.py
```

Your backend will run on `http://localhost:5000`

### Frontend Setup

Open the `index.html` file located in your project folder directly in your web browser, or serve it locally:

```bash
python -m http.server 8000
```

Then, open `http://localhost:8000` in your browser.

## 📝 Usage

- Fill in your resume details in the provided fields.
- Paste your desired job description.
- Click on the **"Generate Tailored Resume"** button.
- Review the tailored resume side-by-side with your original input, along with the processing time.

## 🛠️ Contributing

Feel free to submit issues or pull requests. Contributions are always welcome!

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Built with ❤️ by [Your Name or Organization].

