from logger_config import logger

# This is a simple brain module that generates responses based on user input.
def generate_response(text):
    try:
        response = f"You said: {text}. I'm still learning!"
        return response
    except Exception as e:
        logger.exception("Error in generate_response")
        return "Sorry, I had trouble thinking."
