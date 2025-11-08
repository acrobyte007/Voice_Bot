import logging
import os
from dotenv import load_dotenv
import assemblyai as aai

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def transcribe_audio(audio_file: str) -> str:
    try:
        load_dotenv()
        API_KEY = os.getenv('ASSEMBLY_API_KEY')
        if not API_KEY:
            raise ValueError("ASSEMBLY_API_KEY not found in environment variables.")
        aai.settings.api_key = API_KEY
        logger.info(f"Starting transcription for: {audio_file}")
        transcript = aai.Transcriber().transcribe(audio_file)
        if transcript.status == "error":
            raise RuntimeError(f"Transcription failed: {transcript.error}")
        logger.info("Transcription completed successfully.")
        return transcript.text
    except Exception as e:
        logger.error(f"Error during transcription: {e}")
        return ""

if __name__ == "__main__":
    audio_path = "male_voice.wav"
    text_output = transcribe_audio(audio_path)
    print(text_output)
