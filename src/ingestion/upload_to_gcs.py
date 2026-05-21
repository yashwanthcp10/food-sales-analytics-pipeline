from google.cloud import storage

from tenacity import (
    retry,
    stop_after_attempt,
    wait_fixed
)

import os

from src.utils.logger import setup_logger
from src.utils.config_loader import load_config

logger = setup_logger()

config = load_config()


@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(2)
)
def upload_to_gcs(file_path):

    bucket_name = config["gcp"]["buckets"]["raw"]

    client = storage.Client()

    bucket = client.bucket(
        bucket_name
    )

    file_name = os.path.basename(
        file_path
    )

    blob = bucket.blob(
        file_name
    )

    blob.upload_from_filename(
        file_path
    )

    logger.info(
        f"Uploaded {file_name} "
        f"to GCS bucket "
        f"{bucket_name}"
    )

    return (
        f"gs://{bucket_name}/"
        f"{file_name}"
    )