import yaml
from pathlib import Path


def load_config(config_path="configs/config.yaml"):

    config_file = Path(config_path)

    if not config_file.exists():
        raise FileNotFoundError(
            f"Config file not found: {config_path}"
        )

    with open(config_file, "r") as file:
        config = yaml.safe_load(file)

    return config