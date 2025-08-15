from pydantic import BaseModel
from typing import Optional

class TextRequest(BaseModel):
    text: str

class LLMRequest(BaseModel):
    text: str

class TTSResponse(BaseModel):
    audio_url: Optional[str] = None
    bot_text: Optional[str] = None

class LLMResponse(BaseModel):
    response: str

class AgentChatResponse(BaseModel):
    user_transcript: Optional[str] = None
    bot_text: str
    audio_url: Optional[str] = None