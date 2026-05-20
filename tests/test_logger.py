print("TEST STARTED")

from src.utils.logger import setup_logger

print("IMPORT SUCCESS")

logger = setup_logger()

print("LOGGER CREATED")

logger.info("Pipeline started")
logger.warning("This is warning")
logger.error("This is error")

print("TEST FINISHED")