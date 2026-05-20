import shutil
from pathlib import Path
from datetime import datetime


def archive_file(
    source_path,
    archive_base_path="data/archive"
):
    """
    Move processed files to archive folder.
    """

    current_date = datetime.now()

    year = current_date.strftime("%Y")
    month = current_date.strftime("%m")

    archive_path = Path(
        archive_base_path
    ) / year / month

    archive_path.mkdir(
        parents=True,
        exist_ok=True
    )

    destination = archive_path / Path(source_path).name

    shutil.move(source_path, destination)

    return str(destination)