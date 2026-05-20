from src.utils.logger import setup_logger
from src.ingestion.excel_reader import read_excel_file
from src.quality.validate_file import (
    validate_schema,
    validate_nulls,
    validate_duplicates
)
from src.ingestion.upload_to_gcs import (
    upload_file_to_gcs
)
from src.processing.bronze_load import (
    load_dataframe_to_bigquery
)
from src.ingestion.archive_file import archive_file


logger = setup_logger()


def process_file(file_path):

    try:

        logger.info(
            f"Processing file: {file_path}"
        )

        df = read_excel_file(file_path)

        validate_schema(df)

        validate_nulls(df)

        validate_duplicates(df)

        logger.info("Validation successful")

        gcs_path = upload_file_to_gcs(
            bucket_name="gcs-food-sales-raw-prod",
            source_file_path=file_path,
            destination_blob_name=f"raw/{file_path}"
        )

        logger.info(
            f"Uploaded to GCS: {gcs_path}"
        )

        load_dataframe_to_bigquery(
            dataframe=df,
            table_id=(
                "food-sales-analytics-prod"
                ".food_sales.bronze_orders"
            )
        )

        logger.info(
            "Bronze layer load completed"
        )

        archive_location = archive_file(
            file_path
        )

        logger.info(
            f"File archived: {archive_location}"
        )

    except Exception as error:

        logger.error(
            f"Pipeline failed: {str(error)}"
        )

        raise


if __name__ == "__main__":

    process_file(
        "data/incoming/sample.xlsx"
    )