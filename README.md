# VibeSync — Emotion-Aware Music Player

An AI-powered web application that detects your facial emotion in real time using a CNN trained from scratch, and recommends music to match or lift your mood.

## Live Demo

[vibesync on Vercel](https://vibe-sync-git-main-poorvaja-1603s-projects.vercel.app/)

**Backend API:** https://vibe-sync-hy8w.onrender.com

## How It Works

1. **Show Your Face** — Allow camera access. OpenCV detects your face in real time using Haar Cascade.
2. **AI Reads Your Mood** — A CNN trained from scratch on FER2013 classifies your emotion into one of 6 categories.
3. **Music Plays** — Songs are fetched from JioSaavn matching your mood. Click any song to play on YouTube.

## Tech Stack

| Layer           | Tech                                 |
| --------------- | ------------------------------------ |
| Deep Learning   | PyTorch — CNN trained from scratch   |
| Computer Vision | OpenCV — Haar Cascade face detection |
| Backend         | FastAPI + Uvicorn                    |
| Music API       | JioSaavn (no auth required)          |
| Frontend        | Next.js + Tailwind CSS + Poppins     |
| Deployment      | Vercel (frontend) + Render (backend) |

## Model Details

- **Architecture:** Custom CNN — Conv2D + BatchNorm + ELU + MaxPool
- **Dataset:** FER2013 (35,887 grayscale 48x48 face images)
- **Classes:** 6 emotions — Angry, Fear, Happy, Neutral, Sad, Surprise
- **Test Accuracy:** 65.45%
- **Inference Improvements:**
  - Confidence thresholding — defaults to Neutral if confidence < 45%
  - Majority vote across 5 frame crops — reduces single frame noise

## Emotions Detected

| Emotion  | Music Response                                 |
| -------- | ---------------------------------------------- |
| Happy    | Upbeat party songs to keep the energy up       |
| Sad      | Uplifting feel-good songs to lift your spirits |
| Angry    | Calm and soothing songs to ease the tension    |
| Fear     | Motivational songs to build confidence         |
| Neutral  | Chill lofi beats to vibe to                    |
| Surprise | Energetic trending songs to match the energy   |

## Project Structure

vibesync/
├── ML/
│ ├── emotionNet.py # CNN architecture
│ ├── dataset.py # FER2013 data loading + augmentation
│ ├── train.py # training loop + scheduler
│ ├── detect.py # OpenCV face detection + inference
│ ├── music.py # JioSaavn music fetching
│ ├── main.py # FastAPI backend
│ ├── config.py # hyperparameters + paths
│ ├── Dockerfile # for Render deployment
│ └── requirements.txt
└── Frontend/
├── app/
│ ├── page.js # landing page
│ ├── detect/ # webcam + detection page
│ └── results/ # emotion result + songs page
└── components/
├── Navbar.js
├── EmotionBadge.js # emotion display with color per mood
└── SongCard.js # song card with YouTube link

## Running Locally

### Prerequisites

- Python 3.11+
- Node.js 18+
- CUDA GPU (optional, CPU works too)
- FER2013 dataset from Kaggle

### Backend Setup

```bash
cd ML
python -m venv venv

# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

Download FER2013 from [Kaggle](https://www.kaggle.com/datasets/msambare/fer2013) and place inside `ML/dataset/` with this structure:
ML/dataset/
├── train/
│ ├── angry/
│ ├── fear/
│ ├── happy/
│ ├── neutral/
│ ├── sad/
│ └── surprise/
└── test/
├── angry/
├── fear/
├── happy/
├── neutral/
├── sad/
└── surprise/
Train the model:

```bash
python train.py
```

Start the backend:

```bash
uvicorn main:app --reload --port 8000
```

### Frontend Setup

```bash
cd Frontend
npm install
```

Create `.env.local`:
NEXT_PUBLIC_API_URL=http://localhost:8000

Start the frontend:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

## API Endpoints

| Method | Endpoint           | Description                             |
| ------ | ------------------ | --------------------------------------- |
| GET    | `/`                | Health check                            |
| POST   | `/predict`         | Accepts image → returns emotion + songs |
| GET    | `/songs/{emotion}` | Fetch songs for a given emotion         |

## Future Improvements

- Fine-tune with ResNet18 for higher accuracy
- Real-time webcam streaming instead of single frame capture
- Spotify full playback integration
- Mobile responsive webcam experience
- Emotion history dashboard
- Multi-face detection support

## Built With

- [PyTorch](https://pytorch.org/)
- [OpenCV](https://opencv.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Next.js](https://nextjs.org/)
- [JioSaavn API](https://www.jiosaavn.com/)
- [Render](https://render.com/)
- [Vercel](https://vercel.com/)

## Academic Context

Built as an academic mini-project at **VESIT (Vivekanand Education Society's Institute of Technology)**, Mumbai — Computer Engineering, Semester IV (2024-25).

## License

MIT
