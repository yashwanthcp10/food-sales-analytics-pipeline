import shutil
import os

from datetime import datetime

from src.utils.logger import setup_logger

logger = setup_logger()


def archive_file(file_path):

    file_name = os.path.basename(
        file_path
    )

    year = datetime.now().strftime(
        "%Y"
    )

    month = datetime.now().strftime(
        "%m"
    )

    archive_folder = os.path.join(
        "data/archive",
        year,
        month
    )

    os.makedirs(
        archive_folder,
        exist_ok=True
    )

    destination = os.path.join(
        archive_folder,
        file_name
    )

    shutil.move(
        file_path,
        destination
    )

    logger.info(
        f"Archived file to "
        f"{destination}"
    )