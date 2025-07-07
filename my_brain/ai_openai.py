import os
from openai import OpenAI
from dotenv import load_dotenv
from logger_config import logger
from my_exceptions.my_assistant_exception import LLMFailureException

# Load environment variables
load_dotenv()

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def use_openai(prompt: str) -> str:
    """Send a prompt to OpenAI and return the generated response."""
    try:
        logger.info("Calling OpenAI API...")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        # Try extracting just the message from OpenAI's error
        try:
            message = e.response.json()['error']['message']
        except Exception:
            message = str(e)

        logger.error(f"OpenAI call failed: {message}")
        raise LLMFailureException("I'm having trouble connecting to OpenAI. Please try again later.")
