pip install --upgrade pip
poetry install
# Activate poetry environment
source $(poetry env info --path)/bin/activate

# Update PYTHONPATH to include the virtual environment's Python interpreter
echo "export PYTHON_PATH=$(poetry env info --path)/bin/python" >> ~/.bashrc
#!/bin/bash
# Shebang: tells the system to execute this script using bash

# Exit immediately if any command fails (prevents partial setup)
# This ensures the development environment is either fully set up or fails clearly
set -e

# Display status message to user during container setup
echo "Setting up development environment..."

# Install all dependencies from pyproject.toml and poetry.lock
# --with linting,test includes optional dependency groups for development tools
# This creates the .venv directory and installs packages inside it
poetry install

# Configure shell activation for all future terminal sessions
# This adds a command to .bashrc that automatically activates the Poetry environment
# The '2>/dev/null || true' suppresses errors if Poetry environment doesn't exist yet
echo 'eval "$(poetry env activate)" 2>/dev/null || true' >> ~/.bashrc

# Display completion message to user
echo "Setup complete! Poetry environment activated."