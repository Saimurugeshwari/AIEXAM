from utils.google_speech import synthesize_text

class ReaderAgent:
    def speak(self, text: str):
        print(f"[ReaderAgent] Speaking: {text}")
        synthesize_text(text)
