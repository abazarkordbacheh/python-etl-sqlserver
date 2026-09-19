# python-etl-sqlserver

A layered, testable ETL framework in Python for SQL Server — incremental and full loads,
schema drift detection, idempotent MERGE upserts, and design-pattern-driven architecture.

![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![Tests](https://img.shields.io/badge/tests-pytest-orange?style=flat-square)
![Code style](https://img.shields.io/badge/code%20style-ruff-black?style=flat-square)

---

## Why this project

- **True layered architecture** — Extract, Transform, Validate, Load are independent,
  composable layers; swap any piece without touching the others
- **Incremental & full loads** — watermark stored in a metadata table; no external scheduler needed
- **Idempotent upserts** — MERGE-based loader; re-running a pipeline is always safe
- **Schema drift detection** — column additions, removals, and type changes are caught
  before they break a pipeline
- **Design patterns throughout** — Strategy (transforms), Factory (connections),
  Repository + Unit of Work (load), Template Method (pipeline base), DI at the CLI boundary
- **Real testability** — unit tests run without a database; integration tests use
  Testcontainers with a real SQL Server instance

## Architecture


│ Extract │───▶│ Transform │───▶│ Validation │───▶│ Load │
