# AIEXAM — Inclusive AI-Powered Exam Assistant

**AIEXAM** is a multi-agent exam assistant designed to empower students with disabilities. It supports voice and (future) sign language input, reads questions aloud, captures spoken or typed answers, and logs everything for educators with integrity enforcement. Built using Google Cloud APIs and ADK principles.

##  MVP Focus

This MVP version of AIEXAM supports only **Exam Mode**, prioritizing:
- Accessibility for blind, deaf, and mute students
- Local execution with no cloud storage
- Agent-driven modular design (ADK-style)

*Practice Mode, Clarifier Agents, and Sign Language Input are planned as future enhancements.*

## Core Features (Exam Mode)

- **Reader Agent** — Reads questions aloud using Google Text-to-Speech
- **Listener Agent** — Captures and transcribes spoken answers (Google STT)
- **Formatter Agent** — Cleans and structures answers (spaCy / Gemini)
- **Logger Agent** — Logs answers with timestamps (CSV or JSON)
- **Integrity Agent** — Enforces Exam Mode rules, disables clarifications


## Tech Stack

| Component        | Tool/Library                     |
|------------------|----------------------------------|
| Language         | Python                           |
| APIs             | Google Cloud STT & TTS           |
| NLP              | spaCy, Gemini (optional)         |
| Interface        | Gradio (local testing)           |
| Vision (Future)  | MediaPipe for sign input         |
| Agent Logic      | Modular (ADK-style architecture) |
| Platform         | Local dev via VS Code            |

## Folder Structure

AIEXAM/
├── agents/ # Reader, Listener, Formatter, Logger, Integrity
├── data/ # Input/output files, logs, answers.json
├── notebooks/ # Gemini test notebooks (optional)
├── ui/ # Gradio UI for testing
├── utils/ # Google API wrappers, parsers
├── main.py # Runs the orchestrator
├── requirements.txt
├── .env # Local API credentials
├── README.md

## How to Run

### 1. Install dependencies
-- pip install -r requirements.txt

### Set up Google Cloud
--Create a Service Account (in Google Cloud Console)
--Download the JSON key

### Set env variable:
--export GOOGLE_APPLICATION_CREDENTIALS="path/to/key.json"

### Run the app
--python main.py
--The Gradio UI will launch in your browser.

### Roadmap
Day	   Milestone
1	  Google API setup (STT/TTS)
2	  Core Agents (Reader, Listener, Logger)
3	  Formatter Agent (spaCy)
4+	  Optional UI, Sign Input (MediaPipe)
5+	  OPTIONAL Practice Mode, Clarifier Agent (Gemini)

### Design Sketch:
-- See Design image.png- AIEXAM\Desgin image.png (included in repo)

### License:


### Built For
--Google Cloud Agent Development Kit Hackathon
by Murugeshwari Subramanian

