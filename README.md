# AIEXAM — Inclusive AI-Powered Exam Assistant
AIEXAM is an adaptive, agent-driven exam system designed to empower students with disabilities specifically those who are blind, deaf, or mute. Built using Python and Google Cloud APIs, the tool supports spoken and typed answers, reads questions aloud, and logs responses for educators in a clean, modular fashion.

This project was created for the Google Cloud Agent Development Kit (ADK) Hackathon to showcase how multi-agent systems can simplify real-world challenges in this case, accessible education.

# MVP Focus: Exam Mode Only
This Minimum Viable Product (MVP) focuses only on Exam Mode, with three supported accessibility flows:

-Deaf — Read questions on screen and type answers

-Blind — Questions are read aloud; answers are spoken and transcribed

-Mute — Same as Deaf (type-based input)

# Practice Mode, Clarifier Agents, and Sign Language Input are planned for future updates.

# Features (Multi-Agent Architecture)
Agent	Role Description
    -ReaderAgent	Converts text questions to speech using Google TTS and plays them aloud
    -ListenerAgent	Records user speech and transcribes using Google STT
    -FormatterAgent	Cleans, formats, and prepares answers (via spaCy)
    -LoggerAgent	Logs all answers, timestamps, and disability type to answers.json
    -IntegrityAgent	Placeholder to enforce no-assist rules during exams (MVP stub)

# Tech Stack
    Layer	        Technology
    Language	    Python
    Interface	    Gradio (local UI)
    Agents Logic	Modular ADK-style agents
    Audio APIs	    Google Cloud Speech-to-Text & TTS
    NLP Tools	    spaCy (Gemini planned)
    Vision (Future)	MediaPipe for sign language input
    Audio Control	sounddevice, pygame, scipy.io.wavfile

Deployment	Local execution via VS Code

# Folder Structure
    AIEXAM/
    ├── agents/         # Reader, Listener, Formatter, Logger, Integrity
    ├── data/           # .wav recordings, answers.json, input logs
    ├── notebooks/      # (Optional) NLP experiments
    ├── ui/             # Gradio interface
    ├── utils/          # Google API wrappers, parsers
    ├── main.py         # App entry point
    ├── requirements.txt
    ├── .env            # API keys and secrets
    ├── README.md
# How to Run It Locally
# Install dependencies
    pip install -r requirements.txt
# Set up Google Cloud APIs
    -Create a Service Account via Google Cloud Console
    -Enable:
    -Speech-to-Text API
    -Text-to-Speech API
    -Download your credentials as a .json file

# Configure your environment
    In your .env file:
    GOOGLE_APPLICATION_CREDENTIALS=path/to/your-key.json
# Start the app
    python main.py
    This will launch a Gradio interface at http://127.0.0.1:7860

Architecture Diagram

# Roadmap
Day	Milestone
    1	Google Cloud STT & TTS setup
    2	Core agents: Reader, Listener, Logger
    3	Formatter Agent (spaCy integration)
    4	UI integration with Gradio
    5+	Future ideas: Practice Mode, Sign Input for mute + deaf

# Built By
    -Murugeshwari Subramanian
    -for the Google Cloud Agent Development Kit Hackathon
    -Special thanks to Google Cloud for the tools that made this possible.
