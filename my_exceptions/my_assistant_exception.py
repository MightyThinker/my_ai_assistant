# my_exception/my_assistant_exception.py

class LLMFailureException(Exception):
    """Raised when an LLM fails to generate a valid response."""
    pass
