import json
from pathlib import Path
from datetime import datetime


METADATA_FILE = "data/processed/processed_files.json"


def load_processed_files():

    metadata_path = Path(METADATA_FILE)

    if not metadata_path.exists():
        return {}

    with open(metadata_path, "r") as file:
        return json.load(file)


def save_processed_file(
    file_name,
    checksum
):

    processed_files = load_processed_files()

    processed_files[file_name] = {
        "checksum": checksum,
        "processed_time": str(datetime.now())
    }

    with open(METADATA_FILE, "w") as file:
        json.dump(
            processed_files,
            file,
            indent=4
        )