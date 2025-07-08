# 🌟 Emotion Reflection Tool

A simple web app that allows users to input their feelings in natural language and get an emotion analysis (like “Happy”, “Sad”, “Anxious”) with a confidence score using an AI backend.

---

## ✨ Features

- 📱 Mobile-first clean UI using **Next.js + TypeScript**
- 🧠 Emotion detection powered by **FastAPI + Hugging Face Transformers**
- 🔄 Real-time emotion reflection via API call
- 🎯 Displays emotion and confidence in a styled card
- 🔐 Error handling and loading state support

---

## 🧩 Tech Stack

| Frontend       | Backend        | ML Model (NLP)               |
|----------------|----------------|------------------------------|
| Next.js (TS)   | FastAPI (Python) | distilbert-base-uncased-finetuned-sst-2-english |

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/emotion-reflection-tool.git
cd emotion-reflection-tool

2. Start Backend (FastAPI)
bash
Copy code
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
Server will run at: http://localhost:8000

3. Start Frontend (Next.js)
bash
Copy code
cd frontend
npm install
npm run dev
App runs at: http://localhost:3000

📦 Directory Structure
bash
Copy code
emotion-reflection-tool/
├── backend/              # FastAPI app with transformer model
│   ├── main.py
│   └── requirements.txt
├── frontend/             # Next.js + TypeScript frontend
│   ├── app/
│   └── components/
└── README.md
📽️ Optional Demo Video
👉 Loom Link – short walkthrough of the features and structure.

❌ Exclude From GitHub
Make sure your .gitignore contains:

bash
Copy code
__pycache__/
*.pyc
.env
👨‍💻 Author
Made with ❤️ by
Ansh Verma