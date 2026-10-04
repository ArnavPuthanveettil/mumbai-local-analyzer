"""Central logging configuration for the Mumbai Local analyzer."""

from __future__ import annotations

import logging
import logging.config
from pathlib import Path
from typing import Any, Dict

DEFAULT_LOG_LEVEL = "INFO"


def build_logging_config(log_file: Path) -> Dict[str, Any]:
    """Return a dictConfig-compatible logging configuration.

    Parameters
    ----------
    log_file : Path
        Destination path for application log records.
    """

    log_file.parent.mkdir(parents=True, exist_ok=True)

    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "standard",
                "level": DEFAULT_LOG_LEVEL,
            },
            "file": {
                "class": "logging.FileHandler",
                "formatter": "standard",
                "level": DEFAULT_LOG_LEVEL,
                "filename": str(log_file),
                "encoding": "utf-8",
            },
        },
        "root": {
            "handlers": ["console", "file"],
            "level": DEFAULT_LOG_LEVEL,
        },
    }


def setup_logging(log_file: Path) -> None:
    """Configure logging for the application."""

    config = build_logging_config(log_file)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).debug("Logging configured. Log file: %s", log_file)
