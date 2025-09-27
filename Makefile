.PHONY: help install install-dev clean test lint format db-start db-stop transcribe fetch-coda import-sessions fetch-metadata copy-to-journal

# Load .env file if it exists
ifneq (,$(wildcard .env))
    include .env
    export
endif

help:
	@echo "Available commands:"
	@echo "  make install      - Install project dependencies"
	@echo "  make install-dev  - Install project with dev dependencies"
	@echo "  make clean        - Clean up cache and temporary files"
	@echo "  make test         - Run tests"
	@echo "  make lint         - Run linter (ruff)"
	@echo "  make format       - Format code with black"
	@echo "  make db-start     - Start SurrealDB"
	@echo "  make fetch-coda   - Fetch latest data from Coda API"
	@echo "  make import-sessions - Import sessions from Coda JSON to DB"
	@echo "  make fetch-metadata - Fetch YouTube metadata for sessions"
	@echo "  make transcribe   - Run transcription pipeline (WhisperX)"
	@echo "  make copy-to-journal - Copy transcripts to journal repository"

install:
	uv venv
	. .venv/bin/activate && uv pip install -e .
	. .venv/bin/activate && uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

install-dev:
	uv venv
	. .venv/bin/activate && uv pip install -e ".[dev]"
	. .venv/bin/activate && uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf build dist *.egg-info

test:
	. .venv/bin/activate && python -m pytest tests/

lint:
	. .venv/bin/activate && ruff check src/ tests/

format:
	. .venv/bin/activate && black src/ tests/
	. .venv/bin/activate && ruff check --fix src/ tests/

db-start:
	surreal start --log trace --user root --pass root --bind 0.0.0.0:8080 rocksdb:///mnt/md0/projects/Journal-Utilities/data/database

fetch-coda:
	@echo "Fetching latest data from Coda API..."
	@if [ -z "$(CODA_API_TOKEN)" ]; then \
		echo "Error: CODA_API_TOKEN not found in .env file"; \
		exit 1; \
	fi
	@mkdir -p data/input
	@curl -X GET "https://coda.io/apis/v1/docs/TwB_SP81yq/tables/grid-cjvFiXp3a3/rows?useColumnNames=true" \
		-H "Authorization: Bearer $(CODA_API_TOKEN)" \
		-o data/input/livestream_fulldata_table.json
	@echo "Data saved to data/input/livestream_fulldata_table.json"

import-sessions:
	@echo "Importing sessions from Coda JSON to database..."
	. .venv/bin/activate && cd src && python ingest_db_create_wav.py --step import

fetch-metadata:
	@echo "Fetching YouTube metadata for sessions..."
	. .venv/bin/activate && cd src && python ingest_db_create_wav.py --step metadata

transcribe:
	@echo "Starting transcription pipeline..."
	. .venv/bin/activate && cd src && python transcribe.py

copy-to-journal:
	@echo "Copying transcripts to journal repository..."
	. .venv/bin/activate && cd src && python ingest_db_create_wav.py --step copy