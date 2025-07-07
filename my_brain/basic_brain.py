from logger_config import logger
from my_brain.llm_wrapper import llm_generate_response

def generate_response(text: str) -> str:
    """Generate a response using the underlying LLM (OpenAI or local)."""
    try:
        return llm_generate_response(text)
    except Exception:
        logger.exception("Error in generate_response (basic_brain)")
        return "Sorry, I had trouble thinking."
