import os
import logging
from pathlib import Path
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

from schemas import TextRequest, LLMRequest, TTSResponse, LLMResponse, AgentChatResponse
from services.stt_service import transcribe_audio
from services.tts_service import synthesize_speech
from services.llm_service import query_llm

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

app = FastAPI()

# In-memory chat history store
chat_sessions = {}

# Static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/tts", response_model=TTSResponse)
async def text_to_speech(req: TextRequest):
    try:
        audio_url = synthesize_speech(req.text, style="Promo")
        if audio_url:
            return TTSResponse(audio_url=audio_url)
        else:
            return TTSResponse(audio_url=None, bot_text="I'm having trouble connecting right now.")
    except Exception as e:
        logger.error(f"TTS error: {e}")
        return TTSResponse(audio_url=None, bot_text="I'm having trouble connecting right now.")

@app.post("/llm/query", response_model=LLMResponse)
async def llm_query(req: LLMRequest):
    try:
        answer = query_llm(req.text)
        return LLMResponse(response=answer)
    except Exception as e:
        logger.error(f"LLM error: {e}")
        return LLMResponse(response="I'm having trouble connecting right now.")

@app.post("/agent/chat/{session_id}", response_model=AgentChatResponse)
async def agent_chat(session_id: str, file: UploadFile = File(...)):
    try:
        audio_data = await file.read()
        user_text = transcribe_audio(audio_data)
        if not user_text:
            return AgentChatResponse(
                user_transcript=None,
                bot_text="I'm having trouble connecting right now.",
                audio_url=None
            )

        # Retrieve or create chat history
        history = chat_sessions.get(session_id, [])
        history.append({"role": "user", "text": user_text})

        # Build prompt for LLM
        messages = "\n".join(
            [("User: " + m["text"]) if m["role"] == "user" else ("Bot: " + m["text"]) for m in history]
        )

        bot_text = query_llm(messages)
        history.append({"role": "bot", "text": bot_text})
        chat_sessions[session_id] = history

        audio_url = synthesize_speech(bot_text, style="Conversational")

        return AgentChatResponse(
            user_transcript=user_text,
            bot_text=bot_text,
            audio_url=audio_url
        )
    except Exception as e:
        logger.error(f"Agent chat error: {e}")
        return AgentChatResponse(
            user_transcript=None,
            bot_text="I'm having trouble connecting right now.",
            audio_url=None
        )