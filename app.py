from flask import Flask, render_template, Response, request, jsonify
from flask_cors import CORS
import cv2
from emotion_detector import detect_emotion
from chatbot import get_response

app = Flask(__name__)
CORS(app)

camera = cv2.VideoCapture(0)
latest_emotion = "Neutral"

def generate_frames():
    global latest_emotion

    emotion_colors = {
        "Happy": (0, 255, 0),
        "Sad": (255, 0, 0),
        "Angry": (0, 0, 255),
        "Surprise": (0, 165, 255),
        "Fear": (255, 0, 255),
        "Disgust": (0, 128, 128),
        "Neutral": (128, 128, 128)
    }

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("❌ Failed to access the camera.")
        return

    while True:
        success, frame = camera.read()
        if not success:
            print("❌ Failed to read frame.")
            break

        emotion = detect_emotion(frame)
        latest_emotion = emotion

        color = emotion_colors.get(emotion, (255, 255, 255))
        cv2.putText(
            frame,
            f"Emotion: {emotion}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2,
            cv2.LINE_AA
        )

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    camera.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    print(f"[📨 User input]: {user_input}")
    print(f"[🧠 Emotion detected]: {latest_emotion}")

    # ✅ Inject emotion into chatbot reply
    base_response = get_response(user_input, latest_emotion)

    if latest_emotion == "Happy":
        response = f"😊 You seem cheerful! {base_response}"
    elif latest_emotion == "Sad":
        response = f"😔 I'm here for you. {base_response}"
    elif latest_emotion == "Angry":
        response = f"😠 It's okay to feel that way. Let's take it slow. {base_response}"
    elif latest_emotion == "Neutral":
        response = f"{base_response}"
    else:
        response = f"🤖 {base_response}"

    print(f"[🤖 Bot response]: {response}")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
