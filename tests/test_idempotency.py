from src.ingestion.idempotency import (
    is_file_processed,
    mark_file_processed
)

file_name = (
    "January_23.xlsx"
)

print(
    is_file_processed(
        file_name
    )
)

mark_file_processed(
    file_name
)

print(
    is_file_processed(
        file_name
    )
)