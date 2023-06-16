
import os 
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

def get_audio(user_id, bot_reply):
        
    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"
    current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": ELEVENLABS_API_KEY
    }

    data = {
    "text": bot_reply,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
    }

    response = requests.post(url, json=data, headers=headers)
    file_path = f'audio_outputs/{user_id}/girl.mp3' 
    # Create directories if they don't exist
    os.makedirs(f'audio_outputs/{user_id}', exist_ok=True)

    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
    
    return file_path
