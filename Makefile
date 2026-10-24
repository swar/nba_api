# ============================================================================
# NBA API Makefile - Development Automation
# ============================================================================
#
# USAGE:
#   make <target> [FILES=path/to/file.py]
#
# COMMON TARGETS:
#   make help          - Show all available commands with examples
#   make lint          - Run ruff lint + format check (defaults to the whole repo)
#   make test          - Run all unit tests
#   make test-vcr      - Run cassette-backed integration tests (offline)
#   make test-canary   - Run live canary tests through NBA_API_PROXY (real requests)
#   make check         - Format + lint + unit tests + vcr tests (pre-commit check)
#   make check-package - Build, twine-check, and import the installed wheel
#   make ci            - Same checks as CI, without modifying files
#
# EXAMPLES:
#   make lint FILES=src/nba_api/stats/endpoints/dunkscoreleaders.py
#   make format FILES='src/nba_api/stats/endpoints/dunkscoreleaders.py tests/unit/stats/endpoints/test_dunkscoreleaders.py'
#
# DEFAULTS:
#   FILES defaults to: . (the whole repo, same as CI and pre-commit)
#
# ============================================================================

.PHONY: format lint test test-unit test-vcr test-canary test-cov check-package check ci all install clean build help

# Never let `uv run` re-lock behind your back: a stale uv.lock is an error
# (fix it with `uv lock`).
export UV_LOCKED := 1

# Default paths (can be overridden with FILES=path/to/file.py)
SRC_DIR = src/nba_api
TEST_DIR = tests/unit
FILES ?= .

# Help target
help:
	@echo "NBA API Makefile Commands:"
	@echo ""
	@echo "  make install          - Install dependencies with uv"
	@echo "  make format           - Auto-fix lint issues and format with ruff"
	@echo "  make lint             - Run ruff lint + format check"
	@echo "  make test             - Run all unit tests"
	@echo "  make test-unit        - Run unit tests (same as test)"
	@echo "  make test-vcr         - Run cassette-backed integration tests (offline)"
	@echo "  make test-canary      - Run live canary tests through NBA_API_PROXY (real requests)"
	@echo "  make test-cov         - Run tests with coverage report"
	@echo "  make check-package    - Build, twine-check, and import the installed wheel"
	@echo "  make check            - Run format + lint + unit + vcr tests"
	@echo "  make ci               - Run lint + unit + vcr tests + package check (no formatting, mirrors CI)"
	@echo "  make clean            - Remove cache and build artifacts"
	@echo ""
	@echo "Examples with specific files:"
	@echo "  make lint FILES=src/nba_api/stats/endpoints/dunkscoreleaders.py"
	@echo "  make format FILES=src/nba_api/stats/endpoints/dunkscoreleaders.py"

# Install dependencies
install:
	uv sync --locked

# Auto-fix lint issues (incl. import sorting) and format with ruff
format:
	@echo "Formatting: $(FILES)"
	uv run ruff check --fix $(FILES)
	uv run ruff format $(FILES)

# Lint and verify formatting without modifying files
lint:
	@echo "Linting: $(FILES)"
	uv lock --check
	uv run ruff check $(FILES)
	uv run ruff format --check $(FILES)

# Run all unit tests. --block-network fails any test that opens a real socket.
test-unit:
	uv run pytest $(TEST_DIR) -v --block-network --record-mode=none

# Alias for test-unit
test: test-unit

# Run cassette-backed integration tests. NBA_API_PROXY is blanked so a proxy
# exported in your shell doesn't intercept cassette replay.
test-vcr:
	NBA_API_PROXY= uv run pytest tests/integration -m vcr --block-network --record-mode=none

# Run the live canary tests: real requests to stats.nba.com and cdn.nba.com, always
# through NBA_API_PROXY (skipped when it is unset). Not part of check/ci.
test-canary:
	uv run pytest tests/integration/canary -m canary -v

# Run tests with coverage
test-cov:
	uv run pytest $(TEST_DIR) --cov=$(SRC_DIR) --cov-report=html --cov-report=term

# Build the sdist and wheel, twine-check them, and import the installed wheel
check-package:
	scripts/check-package.sh

# Run all checks (use before committing)
check: format lint test test-vcr

# Run all checks without formatting (for CI)
ci: lint test test-vcr check-package

# Clean up cache and build artifacts
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .coverage htmlcov/ dist/ build/

# Build package
build:
	uv build

# Default target
all: check
