# motoark-data-engineering

MotoArk data engineering: Python + FastAPI + Postgres.

## Layout

- `src/motoark/api` – FastAPI app
- `src/motoark/db` – migrations and database access
- `src/motoark/infra` – fetcher, parser, loader, pipeline
- `tests` – pytest suite

## Local setup

```bash
uv sync
cp .env.example .env   # then edit values
uv run ruff check
uv run mypy
uv run pytest
uv build
uv run uvicorn motoark.api.app:app --reload
```

Requires Python 3.12+, [uv](https://docs.astral.sh/uv/) and a Postgres instance for later units.
