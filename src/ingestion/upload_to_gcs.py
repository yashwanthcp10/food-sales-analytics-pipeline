from google.cloud import storage
from src.utils.retry import retry_on_failure


@retry_on_failure()
def upload_file_to_gcs(
    bucket_name,
    source_file_path,
    destination_blob_name
):

    client = storage.Client()

    bucket = client.bucket(bucket_name)

    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_path)

    return (
        f"gs://{bucket_name}/{destination_blob_name}"
    )