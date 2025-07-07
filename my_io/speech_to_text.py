import speech_recognition as sr
from logger_config import logger

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        logger.info("Listening started...")

        try:
            audio = recognizer.listen(source)
            logger.info("Audio captured, attempting recognition...")
            text = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {text}")
            return text

        except sr.UnknownValueError:
            logger.warning("Speech not understood.")
            return "Sorry, I didn’t catch that."

        except sr.RequestError as e:
            logger.error(f"Speech service request failed: {e}")
            return "Speech recognition service is unavailable."

        except Exception as e:
            logger.exception("Unexpected error in listen()")
            return "An error occurred while listening."
