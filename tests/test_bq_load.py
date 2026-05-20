from src.ingestion.excel_reader import (
    read_excel_file
)

from src.processing.bronze_load import (
    load_dataframe_to_bigquery
)

df = read_excel_file(
    "data/incoming/sample.xlsx"
)

load_dataframe_to_bigquery(
    dataframe=df,
    table_id=(
        "food-sales-analytics-prod"
        ".food_sales.bronze_orders"
    )
)