import logging
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

log_format = "%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"

logging.basicConfig(
    filename="logs/assistant.log",  # moved inside logs/
    filemode="a",
    format=log_format,
    level=logging.INFO
)

logger = logging.getLogger("AssistantLogger")
