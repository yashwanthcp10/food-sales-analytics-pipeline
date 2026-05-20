import pandas as pd


REQUIRED_COLUMNS = [
    "Order_ID",
    "Restaurant_Name",
    "Order_Date",
    "Sales_Amount"
]


def validate_schema(df):

    missing_columns = [
        col for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    return True


def validate_nulls(df):

    critical_columns = [
        "Order_ID",
        "Sales_Amount"
    ]

    for col in critical_columns:

        if df[col].isnull().sum() > 0:

            raise ValueError(
                f"Null values found in {col}"
            )

    return True


def validate_duplicates(df):

    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:

        raise ValueError(
            f"Duplicate rows found: {duplicate_count}"
        )

    return True