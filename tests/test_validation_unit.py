import pandas as pd

from src.quality.validate_file import (
    validate_nulls
)


def test_validate_nulls():

    dataframe = pd.DataFrame({

        "id": [1, 2],

        "name": ["A", "B"]

    })

    result = validate_nulls(
        dataframe
    )

    assert result is True