import os
from openai import OpenAI
from dotenv import load_dotenv
from logger_config import logger

# Load environment variables
load_dotenv()

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def use_openai(prompt: str) -> str:
    """Send a prompt to OpenAI and return the generated response."""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception:
        logger.exception("OpenAI call failed")
        raise  # Let the caller handle the exception (e.g., fallback in llm_wrapper)
