from google.cloud import bigquery
from datetime import datetime
import uuid


def load_dataframe_to_bigquery(
    dataframe,
    table_id
):
    """
    Load dataframe into BigQuery.
    """

    client = bigquery.Client()

    dataframe["load_timestamp"] = datetime.now()

    dataframe["batch_id"] = str(uuid.uuid4())

    job = client.load_table_from_dataframe(
        dataframe,
        table_id
    )

    job.result()

    return "Load completed"