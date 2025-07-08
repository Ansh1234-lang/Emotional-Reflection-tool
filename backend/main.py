from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

# Load the emotion classification pipeline
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/reflect")
def reflect_emotion(text: str = Form(...)):
    predictions = emotion_classifier(text)[0]
    # Get top prediction
    top_emotion = max(predictions, key=lambda x: x['score'])
    return {
        "emotion": top_emotion['label'],
        "confidence": round(top_emotion['score'], 2)
    }

@app.get("/")
def read_root():
    return {
        "message": "Emotion Reflection API running!"
    }
