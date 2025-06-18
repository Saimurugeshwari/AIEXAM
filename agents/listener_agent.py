from utils.google_speech import transcribe_audio
import os

class ListenerAgent:
    def listen(self, audio_file: str = "recorded.wav") -> str:
        print("[ListenerAgent] Transcribing audio...")
        if not os.path.exists(audio_file):
            print("Audio file not found.")
            return ""
        return transcribe_audio(audio_file)
