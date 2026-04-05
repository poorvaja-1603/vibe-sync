import cv2
import torch
import numpy as np
from torchvision import transforms
from emotionNet import EmotionNet
from config import NUM_OF_CHANNELS, NUM_OF_CLASSES, MODEL_SAVE_PATH, EMOTIONS

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((48, 48)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])
])

def load_model():
    model = EmotionNet(
        numOfChannels=NUM_OF_CHANNELS,
        numOfClasses=NUM_OF_CLASSES
    ).to(device)
    model.load_state_dict(
        torch.load(MODEL_SAVE_PATH, map_location=device)
    )
    model.eval()
    return model

def detect_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    if len(faces) == 0:
        return None
    faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)
    return faces[0]

def preprocess_face(frame, face_coords):
    x, y, w, h = face_coords
    face = frame[y:y+h, x:x+w]
    tensor = transform(face)
    tensor = tensor.unsqueeze(0)
    tensor = tensor.to(device)
    return tensor

def predict_emotion(model, face_tensor):
    with torch.no_grad():
        outputs = model(face_tensor)
        probs = torch.softmax(outputs, dim=1)
        confidence, predicted = probs.max(1)

    confidence_val = confidence.item() * 100

    # Fix 1 — confidence threshold
    # if model isn't sure enough → neutral
    if confidence_val < 45:
        return "neutral", confidence_val

    emotion = EMOTIONS[predicted.item()]
    return emotion, confidence_val

def predict_emotion_majority(model, frame, num_frames=5):
    """
    Takes num_frames slightly varied crops of the face
    and returns the majority voted emotion.
    More robust than single frame prediction.
    """
    face_coords = detect_face(frame)
    if face_coords is None:
        return None, None

    x, y, w, h = face_coords
    emotion_counts = {}
    confidences = []

    for i in range(num_frames):
        # slight random crop variation to simulate multiple frames
        jitter = 3
        x2 = max(0, x + np.random.randint(-jitter, jitter))
        y2 = max(0, y + np.random.randint(-jitter, jitter))
        w2 = w + np.random.randint(-jitter, jitter)
        h2 = h + np.random.randint(-jitter, jitter)

        # make sure coords are valid
        x2 = max(0, x2)
        y2 = max(0, y2)
        w2 = max(30, w2)
        h2 = max(30, h2)

        try:
            face = frame[y2:y2+h2, x2:x2+w2]
            if face.size == 0:
                continue

            tensor = transform(face).unsqueeze(0).to(device)
            emotion, confidence = predict_emotion(model, tensor)

            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
            confidences.append(confidence)
        except:
            continue

    if not emotion_counts:
        return None, None

    # pick most common emotion
    final_emotion = max(emotion_counts, key=emotion_counts.get)
    avg_confidence = sum(confidences) / len(confidences) if confidences else 0

    return final_emotion, avg_confidence

def draw_results(frame, face_coords, emotion, confidence):
    x, y, w, h = face_coords
    cv2.rectangle(frame, (x, y), (x+w, y+h), (147, 51, 234), 2)
    label = f"{emotion} ({confidence:.1f}%)"
    cv2.putText(
        frame, label,
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (147, 51, 234),
        2
    )
    return frame

def process_frame(model, frame):
    """
    Uses majority vote for better accuracy.
    Input:  raw webcam frame
    Output: annotated frame + emotion + confidence
    """
    face_coords = detect_face(frame)

    if face_coords is None:
        cv2.putText(frame, "No face detected", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        return frame, None, None

    # use majority vote instead of single prediction
    emotion, confidence = predict_emotion_majority(model, frame, num_frames=5)

    if emotion is None:
        return frame, None, None

    frame = draw_results(frame, face_coords, emotion, confidence)
    return frame, emotion, confidence

if __name__ == '__main__':
    model = load_model()
    cap = cv2.VideoCapture(0)
    print("Press Q to quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame, emotion, confidence = process_frame(model, frame)

        if emotion:
            print(f"Emotion: {emotion} ({confidence:.1f}%)")

        cv2.imshow('Emotion Detector', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()