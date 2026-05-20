from src.utils.logger import setup_logger

logger = setup_logger()

logger.info("Pipeline started")
logger.warning("This is warning")
logger.error("This is error")