import os
from google.cloud import texttospeech, speech
import uuid
import pygame

def synthesize_text(text, output=None):
    client = texttospeech.TextToSpeechClient()

    if output is None:
        output = f"data/output_{uuid.uuid4().hex}.mp3"

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config,
    )

    with open(output, "wb") as out:
        out.write(response.audio_content)
        print(f"[TTS] Audio content written to {output}")

    # Play using pygame
    pygame.mixer.init()
    pygame.mixer.music.load(output)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # smoother loop than `continue`

    # Unload audio and safely delete
    pygame.mixer.music.unload()
    pygame.mixer.quit()

    try:
        os.remove(output)
        print(f"[TTS] Cleaned up {output}")
    except Exception as e:
        print(f"[TTS] Failed to delete {output}: {e}")

def transcribe_audio(audio_file):
    client = speech.SpeechClient()

    with open(audio_file, "rb") as f:
        content = f.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-US",
        audio_channel_count=1
    )

    response = client.recognize(config=config, audio=audio)

    if response.results:
        return response.results[0].alternatives[0].transcript
    else:
        return "[Unrecognized audio]"
