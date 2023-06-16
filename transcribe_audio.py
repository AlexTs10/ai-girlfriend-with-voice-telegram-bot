import openai
import os 
import subprocess
from pydub import AudioSegment
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def oga_2_mp3(filename):
    input_file = f"{filename}.oga"
    output_file = f"{filename}.mp3"

    # Load .oga file
    audio = AudioSegment.from_ogg(input_file)

    # Export as .mp3
    audio.export(output_file, format="mp3")
    # Run the ffmpeg command to convert .oga to .mp3
    #subprocess.run(["ffmpeg", "-i", input_file, "-codec:a", "libmp3lame", "-qscale:a", "2", output_file])


def oga_2_mp3_2_text(filename):

    oga_2_mp3(filename)
    openai.api_key = OPENAI_API_KEY

    audio_file_path = f"{filename}.mp3"
    transcript = None

    try:
        with open(audio_file_path, "rb") as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file, language="en")
            print(transcript)
            print(transcript.text)
    except Exception as e:
        print(f"Transcription failed: {str(e)}")

    # Delete audio files if the transcription was successful
    if transcript:
        os.remove(audio_file_path)
        os.remove(f"{filename}.oga")
        print("Audio files deleted.")

    return transcript.text if transcript else ""
