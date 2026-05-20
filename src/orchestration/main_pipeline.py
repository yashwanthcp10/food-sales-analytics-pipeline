from src.utils.logger import setup_logger
from src.utils.config_loader import load_config


def main():

    logger = setup_logger()

    config = load_config()

    logger.info("Pipeline started")

    logger.info(
        f"Project: {config['project']['name']}"
    )

    logger.info("Pipeline completed")


if __name__ == "__main__":
    main()