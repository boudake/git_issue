
import os
import tomllib
from pathlib import Path
from typing import Any


def load_config(
    config_path: str = "config/application.toml",
) -> dict[str, Any]:
    path = Path(config_path)

    with path.open("rb") as config_file:
        config = tomllib.load(config_file)

    # Allow the deployment environment to override settings.
    config["application"]["environment"] = os.getenv(
        "APP_ENV",
        config["application"]["environment"],
    )

    config["application"]["log_level"] = os.getenv(
        "LOG_LEVEL",
        config["application"]["log_level"],
    )

    return config
