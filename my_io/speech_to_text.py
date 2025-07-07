import speech_recognition as sr
from logger_config import logger

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        logger.info("Listening started...")
        print("🎙️ Listening...")

        try:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)
            logger.info("Audio captured, attempting recognition...")

            text = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {text}")
            return text

        except sr.UnknownValueError:
            logger.warning("Speech not understood.")
            return None

        except sr.RequestError as e:
            logger.error(f"Speech service request failed: {e}")
            return None

        except Exception as e:
            logger.exception("Unexpected error in listen()")
            return None
