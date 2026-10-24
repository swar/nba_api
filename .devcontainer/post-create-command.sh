#!/bin/bash
# Runs once after the dev container is created.

# Exit immediately if any command fails, so the environment is either fully set up or fails clearly.
set -e

echo "Setting up development environment..."

# Create .venv and install the locked dependencies (runtime and dev groups).
uv sync --locked

# Make plain `python`, `pytest` and `ruff` use the project environment in new terminals.
echo 'source /workspace/.venv/bin/activate' >> ~/.bashrc

echo "Setup complete! Run commands with 'uv run <command>' or from an activated shell."
