import os
import socket
from dotenv import load_dotenv
from logger_config import logger
from my_brain.ai_openai import use_openai
from my_brain.ai_ollama import use_ollama

load_dotenv()

# Initialize mode from environment or default to auto
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
        logger.info(f"Generating response in mode: {LLM_MODE}")
        if LLM_MODE == "openai":
            return use_openai(prompt)
        elif LLM_MODE == "local":
            return use_ollama(prompt)
        else:  # AUTO mode
            if is_connected():
                try:
                    return use_openai(prompt)
                except Exception as e:
                    logger.warning(f"OpenAI failed: {e} — falling back to local model.")
                    return use_ollama(prompt)
            else:
                logger.info("Offline — using local model.")
                return use_ollama(prompt)
    except Exception:
        logger.exception("LLM response generation failed")
        return "Sorry, something went wrong while generating a response."

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
