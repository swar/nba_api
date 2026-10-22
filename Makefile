# ============================================================================
# NBA API Makefile - Development Automation
# ============================================================================
#
# USAGE:
#   make <target> [FILES=path/to/file.py]
#
# COMMON TARGETS:
#   make help          - Show all available commands with examples
#   make lint          - Run ruff lint + format check (defaults to all src + tests)
#   make test          - Run all unit tests
#   make test-vcr      - Run cassette-backed integration tests (offline)
#   make check         - Format + lint + unit tests + vcr tests (pre-commit check)
#   make ci            - Same checks as CI, without modifying files
#
# EXAMPLES:
#   make lint FILES=src/nba_api/stats/endpoints/dunkscoreleaders.py
#   make format FILES='src/nba_api/stats/endpoints/dunkscoreleaders.py tests/unit/stats/endpoints/test_dunkscoreleaders.py'
#
# DEFAULTS:
#   FILES defaults to: src/nba_api tests (both source and tests)
#
# ============================================================================

.PHONY: format lint test test-unit test-vcr test-cov check ci all install clean build help

# Default paths (can be overridden with FILES=path/to/file.py)
SRC_DIR = src/nba_api
TEST_DIR = tests/unit
FILES ?= $(SRC_DIR) tests

# Help target
help:
	@echo "NBA API Makefile Commands:"
	@echo ""
	@echo "  make install          - Install dependencies with poetry"
	@echo "  make format           - Auto-fix lint issues and format with ruff"
	@echo "  make lint             - Run ruff lint + format check"
	@echo "  make test             - Run all unit tests"
	@echo "  make test-unit        - Run unit tests (same as test)"
	@echo "  make test-vcr         - Run cassette-backed integration tests (offline)"
	@echo "  make test-cov         - Run tests with coverage report"
	@echo "  make check            - Run format + lint + unit + vcr tests"
	@echo "  make ci               - Run lint + unit + vcr tests (no formatting, mirrors CI)"
	@echo "  make clean            - Remove cache and build artifacts"
	@echo ""
	@echo "Examples with specific files:"
	@echo "  make lint FILES=src/nba_api/stats/endpoints/dunkscoreleaders.py"
	@echo "  make format FILES=src/nba_api/stats/endpoints/dunkscoreleaders.py"

# Install dependencies
install:
	poetry install --sync

# Auto-fix lint issues (incl. import sorting) and format with ruff
format:
	@echo "Formatting: $(FILES)"
	poetry run ruff check --fix $(FILES)
	poetry run ruff format $(FILES)

# Lint and verify formatting without modifying files
lint:
	@echo "Linting: $(FILES)"
	poetry run ruff check $(FILES)
	poetry run ruff format --check $(FILES)

# Run all unit tests
test-unit:
	poetry run pytest $(TEST_DIR) -v

# Alias for test-unit
test: test-unit

# Run cassette-backed integration tests. NBA_API_PROXY is blanked so a local
# .env proxy doesn't intercept cassette replay.
test-vcr:
	NBA_API_PROXY= poetry run pytest tests/integration -m vcr

# Run tests with coverage
test-cov:
	poetry run pytest $(TEST_DIR) --cov=$(SRC_DIR) --cov-report=html --cov-report=term

# Run all checks (use before committing)
check: format lint test test-vcr

# Run all checks without formatting (for CI)
ci: lint test test-vcr

# Clean up cache and build artifacts
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .coverage htmlcov/ dist/ build/

# Build package
build:
	poetry build

# Default target
all: check
