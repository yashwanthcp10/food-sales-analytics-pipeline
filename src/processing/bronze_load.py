import pandas as pd

from google.cloud import bigquery

from src.utils.logger import setup_logger
from src.utils.helpers import (
    current_timestamp,
    generate_batch_id
)

logger = setup_logger()


def load_bronze_layer(
    file_path
):

    dataframe = pd.read_excel(
        file_path
    )

    dataframe["load_timestamp"] = (
        current_timestamp()
    )

    dataframe["batch_id"] = (
        generate_batch_id()
    )

    dataframe["source_file"] = (
        file_path
    )

    client = bigquery.Client()

    table_id = (
        "food-sales-analytics-prod"
        ".food_sales"
        ".bronze_orders"
    )

    job = client.load_table_from_dataframe(
        dataframe,
        table_id
    )

    job.result()

    logger.info(
        "Bronze layer load completed"
    )