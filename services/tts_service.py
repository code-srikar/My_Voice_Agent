import os
import requests

MURF_API_KEY = "ap2_d4e50c58-e9ce-464f-9a84-4feafdf4cc46"

def synthesize_speech(text: str, style: str = "Conversational") -> str:
    try:
        murf_url = "https://api.murf.ai/v1/speech/generate"
        headers = {
            "accept": "application/json",
            "api-key": MURF_API_KEY,
            "Content-Type": "application/json"
        }
        payload = {
            "text": text,
            "voice_id": "en-US-natalie",
            "style": style,
            "format": "mp3"
        }
        resp = requests.post(murf_url, headers=headers, json=payload)
        if resp.status_code == 200:
            return resp.json().get("audioFile")
        return None
    except Exception:
        return None