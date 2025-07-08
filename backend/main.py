from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmotionInput(BaseModel):
    text: str

@app.post("/reflect")
def reflect_emotion(text: str = Form(...)):
    # Simple dummy logic
    if "happy" in text.lower():
        return {"emotion": "Happy 😊"}
    else:
        return {"emotion": "Neutral 😐"}

from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Emotion Reflection API</title>
        </head>
        <body style="font-family: sans-serif; text-align: center; padding: 50px;">
            <h1>🚀 Emotion Reflection API</h1>
            <p>This is a backend service for analyzing emotional reflections.</p>
            <p>Use the <a href="/docs">Swagger UI</a> to test the API.</p>
        </body>
    </html>
    """
