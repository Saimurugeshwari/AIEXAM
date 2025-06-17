# AIEXAM - Inclusive AI-Powered Exam Assistant

AIEXAM is a multi-agent exam assistant designed to empower students with disabilities. It supports voice and sign language input, reads questions aloud, captures answers, enforces exam integrity, and logs everything for educators — all powered by Google Cloud and the Agent Development Kit (ADK).

---

## MVP Focus

This version of AIEXAM focuses **only on Exam Mode** to ensure accessibility and integrity in a time-constrained setting.  
**Practice Mode and Clarifier Agents** are planned as future enhancements if selected or extended beyond the hackathon.

---

## Core Features (Exam Mode)

-  **Reader Agent** — Reads exam questions aloud (Google TTS)
- **Listener Agent** — Captures student answers (Google STT)
- **Formatter Agent** — Cleans and structures answers (spaCy or Gemini)
- **Logger Agent** — Logs answers with timestamps (CSV/JSON)
- **Integrity Agent** — Enforces exam rules by disabling assistance during exams

---

## Tech Stack

- **Language**: Python
- **Platform**: VS Code (Local Dev)
- **Cloud APIs**: Google Cloud Speech-to-Text, Text-to-Speech
- **Agents**: ADK-based modular agent logic
- **Optional UI**: Gradio / Streamlit for testing
- **NLP**: spaCy (MVP), Gemini (optional)
- **Vision**: MediaPipe for future sign input

---

## Folder Structure
AIEXAM/
├── agents/ # Reader, Listener, Formatter, Logger, etc.
├── data/ # Input/output files, logs
├── notebooks/ # Dev notebooks
├── ui/ # Optional interface for testing
├── utils/ # Auth, PDF parsing, configs
├── main.py # Orchestrates agents
├── requirements.txt # Python dependencies
├── .env # Local config (e.g., GCP key path)
├── README.md # Project overview


---

## How to Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

Authenticate Google Cloud:

Create a service account in Google Cloud Console

Download the JSON key

Set the environment variable:

export GOOGLE_APPLICATION_CREDENTIALS="path/to/key.json"

## Run the main script:
python main.py
## Roadmap
Day	Milestone
1	Google API setup + Speech/TTS
2	Core Exam Mode Agents
3	Formatter Agent
TBD	Optional UI + Input Diversity (sign language)
TBD	Practice Mode (future)

## License
MIT (or update to your license)

## Built For
[Agent Development Kit Hackathon] — by [Murugeshwari Subramanian]