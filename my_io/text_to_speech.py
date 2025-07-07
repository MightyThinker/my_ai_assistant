import pyttsx3
from logger_config import logger

def speak(text):
    try:
        print(f"🤖 Assistant: {text}")
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        logger.exception("Unexpected error in speak()")
