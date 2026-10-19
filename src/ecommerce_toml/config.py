import os
import tomllib
from pathlib import Path


def load_config() -> dict:
    environment = os.getenv("APP_ENV", "dev")

    config_files = {
        "dev": "application_dev.toml",
        "prod": "application.toml",
    }

    if environment not in config_files:
        raise ValueError(f"Unsupported APP_ENV: {environment}")

    config_path = (
        Path(__file__).resolve().parents[2]
        / "config"
        / config_files[environment]
    )

    with config_path.open("rb") as file:
        return tomllib.load(file)