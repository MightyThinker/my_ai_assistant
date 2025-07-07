from my_io.speech_to_text import listen
from my_io.text_to_speech import speak
from my_brain.basic_brain import generate_response
from logger_config import logger

def main():
    logger.info("Assistant started. Waiting for user input.")
    print("🤖 Assistant started. Speak something...")

    while True:
        try:
            user_input = listen()

            if user_input.lower() in ["exit", "quit", "stop"]:
                logger.info("User requested exit. Shutting down assistant.")
                speak("Goodbye!")
                break

            response = generate_response(user_input)
            speak(response)

            logger.info(f"User: {user_input} | Response: {response}")

        except Exception as e:
            logger.exception("Unexpected error in main assistant loop.")
            speak("Something went wrong. Please check the logs.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception("Fatal error occurred while starting the assistant.")
        print("A critical error occurred. Please check the assistant.log file.")
