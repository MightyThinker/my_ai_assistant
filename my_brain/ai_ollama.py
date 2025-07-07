import os
import requests
from dotenv import load_dotenv
from logger_config import logger

# Load environment variables
load_dotenv()

OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME", "mistral")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

def use_ollama(prompt: str) -> str:
    """Send prompt to Ollama local model and return response text."""
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=1000
        )
        response.raise_for_status()
        result = response.json()
        return result["response"].strip()
    except Exception:
        logger.exception("Ollama call failed")
        raise
