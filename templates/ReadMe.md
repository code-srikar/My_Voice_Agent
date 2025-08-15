# Voice Agent Web App

A modern, interactive web application that lets users converse with an AI-powered voice agent. Users can speak to the agent, which transcribes their speech, generates intelligent responses using a Large Language Model (LLM), and replies with natural-sounding speech.

---

## Features

- **Voice Conversation:** Tap or press spacebar to record your voice and talk to the agent.
- **Real-Time Transcription:** Your speech is transcribed using AssemblyAI.
- **AI Responses:** The agent uses Google Gemini LLM to generate smart, context-aware replies.
- **Text-to-Speech:** Responses are converted to lifelike audio using Murf.ai.
- **Seamless UI:** Modern, responsive design with conversation history and auto-restart for continuous interaction.
- **Session Tracking:** Each conversation is tracked by a unique session ID.

---

## Architecture Overview

```
[User Browser]
    |
    | 1. Records audio (WebM)
    v
[Frontend (index.html)]
    |
    | 2. Sends audio to FastAPI backend (/agent/chat/{session_id})
    v
[FastAPI Backend (main.py)]
    |
    | 3. Transcribes audio (AssemblyAI)
    | 4. Sends transcript + history to Gemini LLM
    | 5. Converts LLM reply to speech (Murf.ai)
    v
[Frontend]
    |
    | 6. Plays agent's audio reply, shows transcript & response
    v
[User Browser]
```

---

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript (vanilla, no frameworks)
- **Backend:** Python, FastAPI
- **APIs:**
  - [AssemblyAI](https://www.assemblyai.com/) (Speech-to-Text)
  - [Google Gemini](https://ai.google.dev/) (LLM)
  - [Murf.ai](https://murf.ai/) (Text-to-Speech)
- **Templating:** Jinja2
- **Environment:** Works locally or on any server supporting Python 3.8+

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd <repo-folder>
```

### 2. Install Python Dependencies

It's recommended to use a virtual environment:

```sh
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On Mac/Linux

pip install fastapi uvicorn python-dotenv requests assemblyai jinja2
```

### 3. Get API Keys

You need API keys for:
- **AssemblyAI** (Speech-to-Text)
- **Murf.ai** (Text-to-Speech)
- **Google Gemini** (LLM)

Sign up for each service and obtain your API keys.

### 4. Create a `.env` File

In the project root, create a `.env` file:

```
ASSEMBLYAI_API_KEY=your_assemblyai_key
MURF_API_KEY=your_murfai_key
GEMINI_API_KEY=your_gemini_key
```

### 5. Directory Structure

```
AI Voice/
├── main.py
├── .env
├── templates/
│   └── index.html
├── static/
│   └── (optional static files)
├── uploads/
│   └── (auto-created for uploads)
```

### 6. Run the Application

```sh
uvicorn main:app --reload
```

- The app will be available at [http://localhost:8000](http://localhost:8000)

---

## Usage

1. Open [http://localhost:8000](http://localhost:8000) in your browser.
2. Click the **"Tap to Talk"** button or press the **spacebar** to start recording.
3. Speak your message. The agent will process, reply, and play the response.
4. The conversation continues automatically—just keep talking!

---

## How It Works

- **Frontend (`index.html`):**
  - Handles microphone access and audio recording.
  - Sends audio to the backend as a `webm` file.
  - Displays conversation history and plays agent responses.
  - Handles errors and auto-restarts recording for smooth interaction.

- **Backend (`main.py`):**
  - Receives audio, transcribes it with AssemblyAI.
  - Maintains chat history per session.
  - Sends conversation context to Gemini LLM for a reply.
  - Converts the reply to speech using Murf.ai.
  - Returns transcript, agent reply, and audio URL to the frontend.

---

## Customization

- **Voices & Styles:** Change the `voice_id` or `style` in `main.py` for different agent personalities.
- **UI:** Edit `index.html` and CSS for branding or layout changes.
- **LLM Prompting:** Modify how chat history is formatted before sending to Gemini for more advanced behaviors.

---

## Troubleshooting

- **Microphone Issues:** Ensure your browser has permission to access the microphone.
- **API Errors:** Check your `.env` keys and API usage limits.
- **No Audio Playback:** Some browsers block autoplay; click the play button if needed.

---

## License

This project is for educational and prototyping purposes. Check the terms of use for each third-party API.

---

## Credits

- [AssemblyAI](https://www.assemblyai.com/)
- [Murf.ai](https://murf.ai/)
- [Google Gemini](https://ai.google.dev/)
- UI inspired by modern voice assistants.

---

## Contributing

Pull requests and suggestions are welcome! Please open an issue for bugs or feature