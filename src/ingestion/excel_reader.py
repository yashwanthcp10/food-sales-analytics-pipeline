import pandas as pd


def read_excel_file(file_path):
    """
    Reads Excel file into DataFrame.
    """

    df = pd.read_excel(file_path)

    return df