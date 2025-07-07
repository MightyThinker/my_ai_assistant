import logging
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

log_format = "%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"
log_file_path = os.path.join("logs", "assistant.log")

# Create a custom logger
logger = logging.getLogger("AssistantLogger")
logger.setLevel(logging.INFO)

# Prevent duplicate logs if multiple imports
if not logger.handlers:
    # File handler
    file_handler = logging.FileHandler(log_file_path, mode="a")
    file_handler.setFormatter(logging.Formatter(log_format))

    # Optional: Console handler (for debugging while running)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(log_format))

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
