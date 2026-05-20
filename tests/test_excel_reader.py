from src.ingestion.excel_reader import read_excel_file

df = read_excel_file(
    "data/incoming/sample.xlsx"
)

print(df.head())