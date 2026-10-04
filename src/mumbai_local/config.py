"""Application configuration loader."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict

from .logging_setup import setup_logging


@dataclass(frozen=True)
class PathsConfig:
    data_root: Path
    raw_data: Path
    cleaned_data: Path
    processed_data: Path
    demo_data: Path
    database: Path
    logs: Path


@dataclass(frozen=True)
class ScrapingConfig:
    enabled: bool
    base_url: str
    request_timeout: int
    retry_count: int
    retry_backoff_seconds: int
    user_agent: str
    respect_robots_txt: bool


@dataclass(frozen=True)
class SeleniumConfig:
    enabled: bool
    driver: str
    headless: bool
    wait_timeout: int


@dataclass(frozen=True)
class CacheConfig:
    enabled: bool
    expiry_hours: int


@dataclass(frozen=True)
class AppConfig:
    project_name: str
    project_version: str
    paths: PathsConfig
    scraping: ScrapingConfig
    selenium: SeleniumConfig
    cache: CacheConfig

    def ensure_directories(self) -> None:
        for directory in (
            self.paths.data_root,
            self.paths.raw_data,
            self.paths.cleaned_data,
            self.paths.processed_data,
            self.paths.demo_data,
            self.paths.logs.parent,
            Path(self.paths.database).parent,
        ):
            directory.mkdir(parents=True, exist_ok=True)

    def configure_logging(self) -> None:
        setup_logging(self.paths.logs)


def _load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {path}")

    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_config(config_path: Path) -> AppConfig:
    payload = _load_json(config_path)

    project_info = payload.get("project", {})
    name = project_info.get("name", "Mumbai Local Analyzer")
    version = project_info.get("version", "0.0.0")

    paths = payload.get("paths", {})
    scraping = payload.get("scraping", {})
    selenium = payload.get("selenium", {})
    cache = payload.get("cache", {})

    paths_config = PathsConfig(
        data_root=Path(paths.get("data_root", "data")),
        raw_data=Path(paths.get("raw_data", "data/raw")),
        cleaned_data=Path(paths.get("cleaned_data", "data/cleaned")),
        processed_data=Path(paths.get("processed_data", "data/processed")),
        demo_data=Path(paths.get("demo_data", "data/demo")),
        database=Path(paths.get("database", "database/mumbai_local.db")),
        logs=Path(paths.get("logs", "logs/app.log")),
    )

    scraping_config = ScrapingConfig(
        enabled=bool(scraping.get("enabled", False)),
        base_url=str(scraping.get("base_url", "")),
        request_timeout=int(scraping.get("request_timeout", 10)),
        retry_count=int(scraping.get("retry_count", 2)),
        retry_backoff_seconds=int(scraping.get("retry_backoff_seconds", 2)),
        user_agent=str(
            scraping.get(
                "user_agent", "MumbaiLocalAnalyzer/0.1 (contact: unknown@example.com)"
            )
        ),
        respect_robots_txt=bool(scraping.get("respect_robots_txt", True)),
    )

    selenium_config = SeleniumConfig(
        enabled=bool(selenium.get("enabled", False)),
        driver=str(selenium.get("driver", "chrome")),
        headless=bool(selenium.get("headless", True)),
        wait_timeout=int(selenium.get("wait_timeout", 15)),
    )

    cache_config = CacheConfig(
        enabled=bool(cache.get("enabled", True)),
        expiry_hours=int(cache.get("expiry_hours", 12)),
    )

    config = AppConfig(
        project_name=name,
        project_version=version,
        paths=paths_config,
        scraping=scraping_config,
        selenium=selenium_config,
        cache=cache_config,
    )

    config.ensure_directories()
    config.configure_logging()

    return config
