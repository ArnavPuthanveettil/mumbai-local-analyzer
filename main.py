"""Utility script for quick manual testing of configuration loading."""

from __future__ import annotations

from pathlib import Path

from mumbai_local.config import load_config


def main() -> None:
    config = load_config(Path("config.json"))
    print("Loaded configuration:")
    print(config)


if __name__ == "__main__":
    main()
