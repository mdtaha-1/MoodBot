import os
import cohere
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Get Cohere API key from environment
cohere_api_key = os.getenv("COHERE_API_KEY")

# Initialize client
co = cohere.Client(cohere_api_key)

def get_response(user_input, emotion):
    try:
        prompt = f"You are a helpful assistant. The user's current emotion is: {emotion}.\nUser: {user_input}\nAssistant:"
        
        response = co.generate(
            model="command-r-plus",  # Use "command-r" if you're on the free plan
            prompt=prompt,
            max_tokens=100,
            temperature=0.7
        )
        return response.generations[0].text.strip()
    except Exception as e:
        print(f"[❌ Cohere Error]: {e}")
        return "❌ Failed to get a response from MoodBot."
