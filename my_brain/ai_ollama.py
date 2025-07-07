import os
import requests
from dotenv import load_dotenv
from logger_config import logger
from my_exceptions.my_assistant_exception import LLMFailureException

# Load environment variables
load_dotenv()

OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME", "mistral")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

def use_ollama(prompt: str) -> str:
    """Send prompt to Ollama local model and return response text."""
    try:
        logger.info(f"Calling Ollama with model: {OLLAMA_MODEL_NAME}")
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=100
        )
        response.raise_for_status()
        result = response.json()
        return result.get("response", "").strip()

    except requests.exceptions.Timeout:
        message = "Ollama call failed: Request timed out."
        logger.error(message)
        raise LLMFailureException("Local model took too long to respond.")

    except requests.exceptions.ConnectionError:
        message = "Ollama call failed: Could not connect to the local model."
        logger.error(message)
        raise LLMFailureException("I can't reach the local model. Is Ollama running?")

    except requests.exceptions.RequestException as e:
        try:
            error_msg = e.response.json().get("error", str(e))
        except Exception:
            error_msg = str(e)

        logger.error(f"Ollama call failed: {error_msg}")
        raise LLMFailureException("I'm having trouble using the local model.")

    except Exception as e:
        logger.error(f"Unexpected Ollama error: {e}")
        raise LLMFailureException("An unexpected error occurred with the local model.")
