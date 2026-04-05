import io
import base64
import numpy as np
import cv2
from PIL import Image
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from detect import load_model, process_frame
from music import get_songs

app = FastAPI(title="VibeSync API")

# allow Next.js frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000",
                   "https://vibe-sync-chi.vercel.app/",
                   "https://vibe-sync-hy8w.onrender.com"],  # Next.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load model once at startup — not on every request
model = load_model()
print("Model loaded")

class EmotionResponse(BaseModel):
    emotion: str
    confidence: float
    songs: list

class Song(BaseModel):
    name: str
    artist: str
    preview_url: str | None
    album_art: str | None

@app.get("/")
def root():
    return {"message": "VibeSync API running"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Accepts an image file from frontend
    Returns detected emotion + confidence + matching songs
    """
    # read uploaded image bytes
    contents = await file.read()

    # convert bytes → numpy array → opencv frame
    nparr = np.frombuffer(contents, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if frame is None:
        raise HTTPException(status_code=400, detail="Invalid image")

    # run emotion detection
    _, emotion, confidence = process_frame(model, frame)

    if emotion is None:
        raise HTTPException(status_code=400, detail="No face detected")

    # fetch matching songs
    songs = await get_songs(emotion)

    return {
        "emotion": emotion,
        "confidence": round(confidence, 2),
        "songs": songs
    }


@app.get("/songs/{emotion}")
async def songs_by_emotion(emotion: str):
    """
    Fetch songs for a given emotion directly
    Useful for testing without webcam
    """
    valid_emotions = ['angry', 'fear', 'happy', 'neutral', 'sad', 'surprise']
    if emotion not in valid_emotions:
        raise HTTPException(status_code=400, detail=f"Invalid emotion. Choose from {valid_emotions}")

    songs = await get_songs(emotion)
    return {"emotion": emotion, "songs": songs}