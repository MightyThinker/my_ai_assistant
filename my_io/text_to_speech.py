import pyttsx3
from logger_config import logger

# Initialize TTS engine globally
engine = pyttsx3.init()

def speak(text):
    try:
        print(f"🤖 Assistant: {text}")
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        logger.error(f"Text-to-speech error: {e}")
        logger.exception("Unexpected error in speak()")
