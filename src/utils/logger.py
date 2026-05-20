import logging
import os


def setup_logger():

    print("LOGGER FUNCTION EXECUTED")

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("food_sales_pipeline")

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # File Handler
    file_handler = logging.FileHandler(
        "logs/pipeline.log"
    )

    file_handler.setLevel(logging.INFO)

    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()

    console_handler.setLevel(logging.INFO)

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger