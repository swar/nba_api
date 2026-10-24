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

# uv manages Python dependencies and the project's .venv. Copied from the pinned
# official image (keep the version in step with UV_VERSION in .github/workflows/ci.yml).
COPY --from=ghcr.io/astral-sh/uv:0.13.4 /uv /uvx /usr/local/bin/

# uv's cache and the workspace are on different filesystems in a dev container,
# so copy instead of hardlinking (silences uv's warning).
ENV UV_LINK_MODE=copy

# Set the working directory where your project files will be mounted
# This is where VS Code will open and where your code will live
WORKDIR /workspace
