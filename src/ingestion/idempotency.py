import json
import os

from src.utils.logger import setup_logger

logger = setup_logger()

REGISTRY_FILE = (
    "data/processed_files.json"
)


def load_registry():

    if not os.path.exists(
        REGISTRY_FILE
    ):

        return []

    with open(
        REGISTRY_FILE,
        "r"
    ) as file:

        return json.load(file)


def save_registry(registry):

    with open(
        REGISTRY_FILE,
        "w"
    ) as file:

        json.dump(
            registry,
            file,
            indent=4
        )


def is_file_processed(
    file_name
):

    registry = load_registry()

    return file_name in registry


def mark_file_processed(
    file_name
):

    registry = load_registry()

    registry.append(file_name)

    save_registry(registry)

    logger.info(
        f"Marked processed: "
        f"{file_name}"
    )