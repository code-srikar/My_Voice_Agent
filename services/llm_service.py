import os
import requests

GEMINI_API_KEY = "AIzaSyBDf5TtPBJUbiMDzYM4UkGMU6lzxKs1O80"

def query_llm(prompt: str) -> str:
    try:
        gemini_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": GEMINI_API_KEY
        }
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        response = requests.post(gemini_url, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            try:
                return data["candidates"][0]["content"]["parts"][0]["text"]
            except (KeyError, IndexError):
                return "No valid response from LLM."
        return "I'm having trouble connecting right now."
    except Exception:
        return "I'm having trouble connecting right now."