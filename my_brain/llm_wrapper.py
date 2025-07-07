import os
import socket
from dotenv import load_dotenv
from logger_config import logger
from my_io.text_to_speech import speak
from my_brain.ai_openai import use_openai
from my_brain.ai_ollama import use_ollama
from my_exceptions.my_assistant_exception import LLMFailureException

# Load environment variables
load_dotenv()
LLM_MODE = os.getenv("LLM_MODE", "auto").lower()


def is_connected() -> bool:
    """Check internet connectivity by pinging Google's DNS."""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        logger.debug("Internet connection verified.")
        return True
    except OSError:
        logger.debug("No internet connection.")
        return False


def llm_generate_response(prompt: str) -> str:
    """Route the prompt to appropriate LLM based on mode and fallback logic."""
    try:
        logger.info(f"Generating response (mode: {LLM_MODE})")

        # Explicit mode: OpenAI
        if LLM_MODE == "openai":
            logger.info("Trying with OpenAI model...")
            return use_openai(prompt)

        # Explicit mode: Local
        elif LLM_MODE == "local":
            logger.info("Trying with local model...")
            return use_ollama(prompt)

        # Auto mode — attempt OpenAI first, then fallback
        else:
            response = None

            if is_connected():
                try:
                    logger.info("Trying with OpenAI model...")
                    response = use_openai(prompt)
                    logger.info("Success using OpenAI.")
                    return response
                except LLMFailureException as e:
                    logger.warning(f"OpenAI failed: {e}")
                    speak("OpenAI is not available at the moment. Trying with local.")

            try:
                logger.info("Trying with local model...")
                response = use_ollama(prompt)
                logger.info("Success using local model.")
                return response
            except LLMFailureException as e:
                logger.warning(f"Local model failed: {e}")
                speak("Local model is also unavailable. Please check if Ollama is running.")

            # Final fallback if all LLMs failed
            final_msg = (
                "Neither OpenAI nor the local model could be reached. "
                "Please check if your API key is active and ensure Ollama is running in the background."
            )
            logger.error("LLM response generation failed: " + final_msg)
            return final_msg

    except Exception as e:
        logger.error(f"Unexpected error during LLM response generation: {e}")
        return "An unexpected error occurred while generating a response."


def set_mode(mode: str):
    """Set the LLM mode dynamically (openai, local, auto)."""
    global LLM_MODE
    if mode.lower() in {"openai", "local", "auto"}:
        LLM_MODE = mode.lower()
        logger.info(f"LLM mode set to: {LLM_MODE}")
    else:
        logger.warning(f"Invalid mode attempted to set: {mode}")


def get_mode() -> str:
    """Return the current LLM mode."""
    return LLM_MODE
