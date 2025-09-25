.PHONY: help install install-dev clean test lint format db-start db-stop transcribe

help:
	@echo "Available commands:"
	@echo "  make install      - Install project dependencies"
	@echo "  make install-dev  - Install project with dev dependencies"
	@echo "  make clean        - Clean up cache and temporary files"
	@echo "  make test         - Run tests"
	@echo "  make lint         - Run linter (ruff)"
	@echo "  make format       - Format code with black"
	@echo "  make db-start     - Start SurrealDB"
	@echo "  make db-stop      - Stop SurrealDB"
	@echo "  make transcribe   - Run transcription pipeline"

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

db-stop:
	pkill -f "surreal start" || true

transcribe:
	@echo "Starting transcription pipeline..."
	. .venv/bin/activate && cd src && python ingest_db_create_wav.py
	. .venv/bin/activate && cd src && python transcribe.py