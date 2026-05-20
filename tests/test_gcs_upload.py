from src.ingestion.upload_to_gcs import (
    upload_file_to_gcs
)

upload_file_to_gcs(
    bucket_name="gcs-food-sales-raw-prod",
    source_file_path="data/incoming/sample.xlsx",
    destination_blob_name="raw/sample.xlsx"
)