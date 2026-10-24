#!/bin/bash
# Runs once after the dev container is created.

# Exit immediately if any command fails, so the environment is either fully set up or fails clearly.
set -e

echo "Setting up development environment..."

# Install the locked dependencies (runtime and dev groups) into the container's own
# virtualenv, UV_PROJECT_ENVIRONMENT (set in the Dockerfile).
uv sync --locked

# Make plain `python`, `pytest` and `ruff` use that environment in new terminals.
activate="source ${UV_PROJECT_ENVIRONMENT}/bin/activate"
grep -qxF "$activate" ~/.bashrc || echo "$activate" >> ~/.bashrc

echo "Setup complete! Run commands with 'uv run <command>' or from an activated shell."
