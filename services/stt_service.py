import os
import assemblyai as aai

aai.settings.api_key = "1fbfca2263ea40dea8b966676162e7a3"

def transcribe_audio(audio_data: bytes) -> str:
    try:
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(audio_data)
        return transcript.text.strip()
    except Exception:
        return None