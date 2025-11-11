# Specify the Python version and base OS for the container
# VARIANT allows customization of Python version (default: 3.10 on Debian Bullseye)
ARG VARIANT="3.10-bullseye"

# Use Microsoft's official Python dev container as the base image
FROM mcr.microsoft.com/devcontainers/python:1-${VARIANT}

# Install system packages as root user before switching to vscode
# - ODBC drivers for SQL Server connectivity
# - GitHub CLI for PR management and git workflows
RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
    && curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | tee /usr/share/keyrings/githubcli-archive-keyring.gpg > /dev/null \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && apt-get update \
    && apt-get install -y gh \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Switch from root to the vscode user for security and proper file permissions
# The vscode user is pre-configured in the base image with development tools
USER vscode

# Download and install Poetry package manager for the vscode user
# Poetry manages Python dependencies and virtual environments
RUN curl -sSL https://install.python-poetry.org -o /tmp/install-poetry.py \
    && python3 /tmp/install-poetry.py \
    && rm /tmp/install-poetry.py

# Add Poetry's installation directory to the system PATH
# This allows the 'poetry' command to be run from anywhere
ENV PATH="/home/vscode/.local/bin:$PATH"

# Configure Poetry to create virtual environments inside the project directory
# This creates a .venv folder in your project root instead of Poetry's global cache
# This setting acts as a "gate" - it ensures proper environment setup before shells can run
# Set cache directory to /tmp to enable fast package downloads during build
# while preventing cache bloat in the final Docker image
RUN poetry config virtualenvs.in-project true \
    && poetry config cache-dir /tmp/poetry_cache

# Set the working directory where your project files will be mounted
# This is where VS Code will open and where your code will live
WORKDIR /workspace