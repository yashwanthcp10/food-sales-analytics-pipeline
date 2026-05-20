import shutil
from pathlib import Path


def move_bad_file(
    source_path,
    bad_folder="data/bad_files"
):
    """
    Move invalid files to bad_files folder.
    """

    Path(bad_folder).mkdir(
        parents=True,
        exist_ok=True
    )

    destination = (
        Path(bad_folder)
        / Path(source_path).name
    )

    shutil.move(source_path, destination)

    return str(destination)