import time
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from src.utils.logger import setup_logger

from src.ingestion.idempotency import (
    is_file_processed,
    mark_file_processed
)

from src.quality.validate_file import (
    validate_file
)

from src.utils.archive import (
    archive_file
)

logger = setup_logger()


class NewFileHandler(
    FileSystemEventHandler
):

    def on_created(self, event):

        # Ignore folders
        if event.is_directory:
            return

        file_path = event.src_path

        file_name = os.path.basename(
            file_path
        )

        logger.info(
            f"New file detected: "
            f"{file_name}"
        )

        # Check idempotency
        if is_file_processed(
            file_name
        ):

            logger.warning(
                f"Skipping already "
                f"processed file: "
                f"{file_name}"
            )

            return

        # Validate file
        validation_result = (
            validate_file(
                file_path
            )
        )

        if not validation_result:

            logger.error(
                f"Validation failed: "
                f"{file_name}"
            )

            return

        logger.info(
            f"Processing started "
            f"for {file_name}"
        )

        # Mark processed
        mark_file_processed(
            file_name
        )

        # Archive file
        archive_file(
            file_path
        )


def start_watching():

    folder_to_watch = (
        "data/incoming"
    )

    event_handler = (
        NewFileHandler()
    )

    observer = Observer()

    observer.schedule(
        event_handler,
        folder_to_watch,
        recursive=False
    )

    observer.start()

    logger.info(
        "Started watching folder"
    )

    try:

        while True:

            time.sleep(5)

    except KeyboardInterrupt:

        observer.stop()

    observer.join()


if __name__ == "__main__":

    start_watching()