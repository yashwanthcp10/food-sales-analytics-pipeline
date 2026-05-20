import hashlib
from pathlib import Path


def generate_file_checksum(file_path):
    """
    Generate SHA256 checksum for file.
    Used for idempotency.
    """

    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as file:

        for block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(block)

    return sha256_hash.hexdigest()


def get_file_extension(file_path):
    """
    Returns file extension.
    """

    return Path(file_path).suffix