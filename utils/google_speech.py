import os
from google.cloud import texttospeech, speech

def synthesize_text(text, output="output.mp3"):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code="en-US")
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open(output, "wb") as out:
        out.write(response.audio_content)

    # Play audio (Windows/macOS/Linux)
    os.system(f"start {output}" if os.name == "nt" else f"afplay {output}" if os.uname().sysname == "Darwin" else f"mpg123 {output}")

def transcribe_audio(audio_file):
    client = speech.SpeechClient()
    with open(audio_file, "rb") as f:
        audio = speech.RecognitionAudio(content=f.read())

    config = speech.RecognitionConfig(
        language_code="en-US",
        audio_channel_count=1
    )

    response = client.recognize(config=config, audio=audio)
    return response.results[0].alternatives[0].transcript if response.results else ""
