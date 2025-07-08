from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmotionInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze_emotion(data: EmotionInput):
    return {"emotion": "Anxious", "confidence": 0.85}
