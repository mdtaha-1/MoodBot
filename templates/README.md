# MoodBot 🤖🎭

MoodBot is an AI-powered chatbot that detects your current emotion using facial recognition and responds accordingly. It uses OpenCV for emotion detection, Cohere for chat replies.

---

## 🧰 Tech Stack

- Python 3.8+
- Flask
- OpenCV
- Cohere API (for smart chatbot responses)
- HTML + JS (frontend animations)
- dotenv (for API key management)

---

## 🚀 Getting Started

### 1️⃣. Install Python 🐍

If you don’t have Python installed:

👉 Download it from [https://www.python.org/downloads](https://www.python.org/downloads/release/python-3109/)  
⚠️ Make sure to check **"Add Python to PATH"** during installation.

Verify installation:

````bash

   python --version


### 2️⃣. Create Virtual Environment

```bash

    python -m venv venv

    venv\Scripts\activate


### 🔑3️⃣. Set Up Cohere API Key (Can also use OpenAI API Key)

If you're using Cohere for chatbot responses, follow this:

### 📋 Get Your API Key

1. Go to [https://dashboard.cohere.com/api-keys](https://dashboard.cohere.com/api-keys)
2. Log in and create an API key.

### 🔐 Save the API Key Securely

Create a `.env` file in the root of your project and add the following:

```env
COHERE_API_KEY=your_api_key_here

Optional: Test API is working or not (test_cohere.py)

```bash

   python test_cohere.py

### 4️⃣. Install Dependencies

```bash

   pip install flask opencv-python

Optional (Recommended): To install from requirements.txt if available:

```bash

   pip install -r requirements.txt

### 5️⃣. Run the Application
```bash

   python app.py

Once the app starts, open your browser and go to:

   http://127.0.0.1:5000
````
