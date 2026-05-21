from src.ingestion.upload_to_gcs import (
    upload_to_gcs
)

file_path = (
    "data/incoming/January_23.xlsx"
)

gcs_path = upload_to_gcs(
    file_path
)

print(gcs_path)