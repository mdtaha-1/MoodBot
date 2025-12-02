# Existing imports
import numpy as np
from keras.models import load_model
import cv2

# Load the model (this is already there)
model = load_model("fer2013_mini_XCEPTION.102-0.66.hdf5", compile=False)
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# ✅ Add a mapping to reduce categories
emotion_map = {
    "Happy": "Happy",
    "Sad": "Sad",
    "Angry": "Angry",
    "Disgust": "Angry",    # map Disgust to Angry
    "Fear": "Sad",         # map Fear to Sad
    "Surprise": "Happy",   # map Surprise to Happy
    "Neutral": "Neutral"
}

def detect_emotion(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (64, 64))
        roi = roi_gray.astype("float") / 255.0
        roi = np.expand_dims(roi, axis=0)
        roi = np.expand_dims(roi, axis=-1)

        prediction = model.predict(roi)[0]
        label = emotion_labels[np.argmax(prediction)]

        # ✅ Map to simplified emotion
        mapped_emotion = emotion_map.get(label, "Neutral")
        return mapped_emotion

    return "Neutral"

# ✅ TEMPORARY CAMERA TEST
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Failed to access the camera. Check if it's connected or already in use.")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame from webcam.")
            break

        emotion = detect_emotion(frame)
        cv2.putText(frame, emotion, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 2)
        cv2.imshow("Mood Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
