import pandas as pd


REQUIRED_COLUMNS = [
    "Order_ID",
    "Restaurant_Name",
    "Order_Date",
    "Sales_Amount"
]


def validate_schema(df):
    """
    Validate required columns.
    """

    missing_columns = [
        col for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    return True