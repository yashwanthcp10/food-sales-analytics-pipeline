import pandas as pd

from src.quality.validate_file import validate_schema


data = {
    "Order_ID": [1],
    "Restaurant_Name": ["ABC"],
    "Order_Date": ["2024-01-01"],
    "Sales_Amount": [100]
}

df = pd.DataFrame(data)

print(validate_schema(df))