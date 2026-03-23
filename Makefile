# ============================================================================
# NBA API Makefile - Development Automation
# ============================================================================
#
# USAGE:
#   make <target> [FILES=path/to/file.py]
#
# COMMON TARGETS:
#   make help          - Show all available commands with examples
#   make lint          - Run flake8 + pylint (defaults to all src + tests)
#   make test          - Run all unit tests
#   make check         - Format + lint + test (pre-commit check)
#
# EXAMPLES:
#   # Lint all source code only
#   make lint FILES=src/nba_api
#
#   # Lint all tests only
#   make lint FILES=tests/unit
#
#   # Lint specific file
#   make lint FILES=src/nba_api/stats/endpoints/dunkscoreleaders.py
#
#   # Lint multiple files (quote the list)
#   make lint FILES='src/nba_api/stats/endpoints/dunkscoreleaders.py tests/unit/stats/endpoints/test_dunkscoreleaders.py'
#
#   # Format before committing
#   make format FILES=src/nba_api/stats/endpoints/dunkscoreleaders.py
#
#   # Run only pylint on specific files
#   make lint-pylint FILES=src/nba_api/stats/endpoints/dunkscoreleaders.py
#
# DEFAULTS:
#   FILES defaults to: src/nba_api tests/unit (both source and tests)
#
# ============================================================================

.PHONY: format lint lint-pylint lint-flake8 test test-unit test-cov check all install clean help

# Default paths (can be overridden with FILES=path/to/file.py)
SRC_DIR = src/nba_api
TEST_DIR = tests/unit
FILES ?= $(SRC_DIR) $(TEST_DIR)

# Help target
help:
	@echo "NBA API Makefile Commands:"
	@echo ""
	@echo "  make install          - Install dependencies with poetry"
	@echo "  make format          - Format code with black and isort"
	@echo "  make lint            - Run all linters (flake8 + pylint)"
	@echo "  make lint-flake8     - Run only flake8"
	@echo "  make lint-pylint     - Run only pylint"
	@echo "  make test            - Run all unit tests"
	@echo "  make test-unit       - Run unit tests (same as test)"
	@echo "  make test-cov        - Run tests with coverage report"
	@echo "  make check           - Run format + lint + test"
	@echo "  make ci              - Run lint + test (no formatting)"
	@echo "  make clean           - Remove cache and build artifacts"
	@echo ""
	@echo "Examples with specific files:"
	@echo "  make lint FILES=src/nba_api/stats/endpoints/dunkscoreleaders.py"
	@echo "  make lint-pylint FILES='src/nba_api/stats/endpoints/dunkscoreleaders.py tests/unit/stats/endpoints/test_dunkscoreleaders.py'"
	@echo "  make format FILES=src/nba_api/stats/endpoints/dunkscoreleaders.py"

# Install dependencies
install:
	poetry install --sync

# Format code with isort and black (isort first to take precedence)
format:
	@echo "Formatting: $(FILES)"
	poetry run isort $(FILES)
	poetry run black $(FILES)

# Run flake8 linter
lint-flake8:
	@echo "Running flake8 on: $(FILES)"
	poetry run flake8 $(FILES)

# Run pylint
lint-pylint:
	@echo "Running pylint on: $(FILES)"
	poetry run pylint $(FILES) || true

# Run all linters
lint: lint-flake8 lint-pylint

# Run all unit tests
test-unit:
	poetry run pytest $(TEST_DIR) -v

# Alias for test-unit
test: test-unit

# Run tests with coverage
test-cov:
	poetry run pytest $(TEST_DIR) --cov=$(SRC_DIR) --cov-report=html --cov-report=term

# Run all checks with only unit tests (fast, use before committing)
check: format lint test

# Run all checks without formatting (for CI)
ci: lint test

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
