# Mumbai Local Train Route and Station Connectivity Analyzer

This repository contains the source code for an academic-scale Python project that analyses Mumbai's suburban railway network. The goal is to ingest publicly accessible railway information, transform it into a clean dataset, and deliver route, station, and connectivity analytics along with static and interactive visualizations.

## Project status

| Phase | Scope | Status |
| --- | --- | --- |
| 1 | Project architecture, configuration, logging and base tests | ✅ In progress on feature/python-analyzer |
| 2 | SQLite schema and database manager | ⏳ Planned |
| 3 | Responsible web scraping (Requests first, Selenium when required) | ⏳ Planned |
| 4 | Data cleaning & validation pipelines | ⏳ Planned |
| 5 | Database integration and caching | ⏳ Planned |
| 6 | Route discovery & ranking | ⏳ Planned |
| 7 | Connectivity metrics & NumPy scoring | ⏳ Planned |
| 8 | Matplotlib analytical charts | ⏳ Planned |
| 9 | Plotly interactive network visualization | ⏳ Planned |
| 10 | Streamlit dashboard | ⏳ Planned |
| 11 | Automated tests and CI workflow | ⏳ Planned |
| 12 | README, documentation & viva guide | ⏳ Planned |

The live M-Indicator source has not yet been inspected in this repository revision. Until its access conditions are reviewed and respected, the pipeline will rely on cached datasets or explicitly labelled demo data.

## Seeking data ethically

This project will only collect data that is publicly accessible and allowed for automated access. It will respect:

- robots.txt
- terms of use
- rate limits
- authentication requirements
- anti-bot or anti-scraping protections

If a page requires manual access, the project supports importing manually downloaded files instead of scraping.

## High-level workflow

```
Public source → Scraper → Cleaner → Validator → SQLite database
           ↘                              ↘
            Fallback CSV / demo data       Export / Visualize
```

Downstream analysis modules provide:

- Station statistics (degree, line coverage, interchange potential)
- Route analysis and multi-route comparisons
- Network-level connectivity indicators
- Matplotlib summaries (line distribution, degree distribution, etc.)
- Plotly-based interactive network visualization
- Streamlit dashboard for exploration

## Current repository structure

```
.
├── README.md
├── app.py                    # Streamlit dashboard (phase 10)
├── config.json               # Central configuration
├── main.py                   # CLI entry point
├── pyproject.toml            # Packaging metadata & tooling configuration
├── requirements-dev.txt      # Developer-only dependencies
├── requirements.txt          # Application dependencies
├── src/
│   └── mumbai_local/
│       ├── __init__.py
│       ├── config.py
│       ├── logging_setup.py
│       ├── analysis/
│       │   ├── __init__.py
│       │   ├── network.py
│       │   ├── route_analysis.py
│       │   └── station_analysis.py
│       ├── pipeline.py
│       ├── processing/
│       │   ├── __init__.py
│       │   ├── cleaner.py
│       │   └── validator.py
│       ├── scraper/
│       │   ├── __init__.py
│       │   ├── bs4_parser.py
│       │   ├── local_import.py
│       │   ├── policy.py
│       │   ├── requests_scraper.py
│       │   └── selenium_scraper.py
│       ├── storage/
│       │   ├── __init__.py
│       │   ├── cache.py
│       │   ├── db_manager.py
│       │   └── schema.sql
│       ├── visualization/
│       │   ├── __init__.py
│       │   ├── matplotlib_charts.py
│       │   └── plotly_charts.py
│       └── exports.py
├── tests/
│   ├── fixtures/
│   │   └── public_table_sample.html
│   ├── test_cleaner.py
│   ├── test_config.py
│   ├── test_connectivity.py
│   ├── test_database.py
│   ├── test_pipeline.py
│   ├── test_routes.py
│   └── test_validator.py
└── data/
    ├── README.md
    ├── demo/
    │   ├── connections.csv
    │   ├── metadata.json
    │   ├── route_stops.csv
    │   ├── routes.csv
    │   └── stations.csv
    ├── raw/
    ├── cleaned/
    └── processed/
```

Files shown in italics (or phases beyond 1) do not exist yet—they are placeholders to illustrate the intended design. They will be introduced in their respective phases with full explanations and tests.

## Next steps

1. Complete Phase 1 (configuration, logging, config tests).
2. Define the normalized SQLite schema and database initialization (Phase 2).
3. Add responsible scraping, manual import, and caching (Phase 3).

Each subsequent phase will:

- add new modules with documentation and tests
- extend the CI workflow
- keep the pipeline functional without fabricating railway data

## Repository governance

- `main` stays stable; all work happens in feature branches.
- Pull requests will include tests, lint output, and documentation updates.
- No sensitive credentials are stored in the repository.

---

© 2026 AshnaAI. Project by Ashna-X1 (ChatGPT) for Arnav Puthanveettil.
