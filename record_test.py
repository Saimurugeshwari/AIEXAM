import sounddevice as sd
from scipy.io.wavfile import write

print("Recording... please speak.")
fs = 44100  # Sample rate
duration = 5  # seconds

recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()

write("test.wav", fs, recording)
print("Saved as test.wav")
