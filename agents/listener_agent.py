import os
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

class ListenerAgent:
    def __init__(self, sample_rate=44100, duration=5):
        self.sample_rate = sample_rate
        self.duration = duration
        self.session_audio = []  # hold audio chunks

    def record_audio(self):
        print("Recording... Please speak now.")
        recording = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=1)
        sd.wait()
        self.session_audio.append(recording)
        print("Recording chunk saved.")

    def save_session(self, path="data/exam_session.wav"):
        if self.session_audio:
            combined = np.concatenate(self.session_audio, axis=0)
            write(path, self.sample_rate, (combined * 32767).astype(np.int16))
            print(f"Full exam audio saved as {path}")

    def listen(self):
        self.record_audio()
        temp_path = "data/temp.wav"
        # Save current chunk temporarily to transcribe
        write(temp_path, self.sample_rate, (self.session_audio[-1] * 32767).astype(np.int16))

        from utils.google_speech import transcribe_audio
        transcript = transcribe_audio(temp_path)
    # Optional: delete temp file after use
        if os.path.exists(temp_path):
            os.remove(temp_path)
        print(f"[ListenerAgent] Transcript: {transcript}")
        return transcript


