"""Ensure configuration loading behaves as expected."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from mumbai_local.config import AppConfig, load_config


@pytest.fixture()
def temp_config(tmp_path: Path) -> Path:
    payload = {
        "project": {"name": "Test Analyzer", "version": "1.2.3"},
        "paths": {
            "data_root": str(tmp_path / "data"),
            "raw_data": str(tmp_path / "data" / "raw"),
            "cleaned_data": str(tmp_path / "data" / "cleaned"),
            "processed_data": str(tmp_path / "data" / "processed"),
            "demo_data": str(tmp_path / "data" / "demo"),
            "database": str(tmp_path / "database" / "railway.db"),
            "logs": str(tmp_path / "logs" / "app.log"),
        },
        "scraping": {
            "enabled": False,
            "base_url": "https://example.com",
            "request_timeout": 5,
            "retry_count": 1,
            "retry_backoff_seconds": 1,
            "user_agent": "TestAgent/1.0",
            "respect_robots_txt": True,
        },
        "selenium": {
            "enabled": False,
            "driver": "firefox",
            "headless": True,
            "wait_timeout": 20,
        },
        "cache": {"enabled": True, "expiry_hours": 6},
    }

    config_path = tmp_path / "config.json"
    config_path.write_text(json.dumps(payload), encoding="utf-8")
    return config_path


def test_load_config_creates_directories_and_returns_dataclass(
    temp_config: Path,
) -> None:
    config = load_config(temp_config)

    assert isinstance(config, AppConfig)
    assert config.project_name == "Test Analyzer"
    assert config.project_version == "1.2.3"

    assert config.paths.data_root.exists()
    assert config.paths.logs.parent.exists()


def test_missing_config_file_raises_file_not_found(tmp_path: Path) -> None:
    missing_path = tmp_path / "missing.json"
    with pytest.raises(FileNotFoundError):
        load_config(missing_path)
