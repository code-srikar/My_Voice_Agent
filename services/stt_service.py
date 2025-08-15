import os
import assemblyai as aai

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

def transcribe_audio(audio_data: bytes) -> str:
    try:
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(audio_data)
        return transcript.text.strip()
    except Exception:
        return None