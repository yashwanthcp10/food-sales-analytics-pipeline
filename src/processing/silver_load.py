import pandas as pd

from google.cloud import bigquery

from src.utils.logger import setup_logger

logger = setup_logger()


def load_silver_layer():

    logger.info(
        "Silver layer processing started"
    )

    client = bigquery.Client()

    query = """

    SELECT *
    FROM `food-sales-analytics-prod.food_sales.bronze_orders`

    """

    dataframe = client.query(
        query
    ).to_dataframe()

    logger.info(
        f"Records fetched from bronze: "
        f"{len(dataframe)}"
    )

    # -----------------------------------
    # Remove duplicates
    # -----------------------------------

    dataframe = dataframe.drop_duplicates()

    logger.info(
        f"Records after deduplication: "
        f"{len(dataframe)}"
    )

    # -----------------------------------
    # Remove null order IDs
    # -----------------------------------

    dataframe = dataframe[
        dataframe["order_id"].notnull()
    ]

    # -----------------------------------
    # Fill null quantity
    # -----------------------------------

    dataframe["quantity"] = (
        dataframe["quantity"]
        .fillna(0)
    )

    # -----------------------------------
    # Standardize payment method
    # -----------------------------------

    dataframe["payment_method"] = (
        dataframe["payment_method"]
        .str.upper()
    )

    # -----------------------------------
    # Convert orderDate
    # -----------------------------------

    dataframe["orderDate"] = pd.to_datetime(
        dataframe["orderDate"],
        errors="coerce"
    )

    # -----------------------------------
    # Remove invalid quantities
    # -----------------------------------

    dataframe = dataframe[
        dataframe["quantity"] > 0
    ]

    logger.info(
        f"Records after cleaning: "
        f"{len(dataframe)}"
    )

    # -----------------------------------
    # Target silver table
    # -----------------------------------

    table_id = (

        "food-sales-analytics-prod"
        ".food_sales"
        ".silver_orders"

    )

    job = client.load_table_from_dataframe(
        dataframe,
        table_id
    )

    job.result()

    logger.info(
        "Silver layer load completed"
    )