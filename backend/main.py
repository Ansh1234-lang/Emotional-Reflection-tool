from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
import logging

# Load sentiment analysis pipeline once
sentiment_analyzer = pipeline("sentiment-analysis")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)

@app.post("/reflect")
def reflect_emotion(text: str = Form(...)):
    result = sentiment_analyzer(text)[0]  # e.g., {'label': 'POSITIVE', 'score': 0.9998}

    if result["label"] == "POSITIVE":
        emotion = "Positive 🙂"
    elif result["label"] == "NEGATIVE":
        emotion = "Negative 😞"
    else:
        emotion = "Neutral 😐"

    return {"emotion": f"{emotion} (Confidence: {round(result['score'] * 100, 2)}%)"}
