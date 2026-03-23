#!/bin/bash

# Script to prepare a release for nba_api
# This automates the changelog generation and version bumping process
# for contributors working on forks

# Wrap everything in a function to avoid exit statements
run_release_prep() {
    echo "NBA API Release Preparation Script"
    echo "======================================"
    echo ""

    # Check if we're in the project root
    if [ ! -f "pyproject.toml" ]; then
        echo "Error: pyproject.toml not found. Please run this script from the project root."
        return 1
    fi

    # Check if poetry is available
    if ! command -v poetry &> /dev/null; then
        echo "Error: poetry is not installed. Please install poetry first."
        return 1
    fi

    # Check current branch
    CURRENT_BRANCH=$(git branch --show-current)
    echo "Current branch: $CURRENT_BRANCH"

    # Check if we're on a release-compatible branch
    if [[ ! "$CURRENT_BRANCH" =~ ^(release|release/.*) ]]; then
        echo ""
        echo "Warning: You're not on a release branch."
        echo "Semantic-release is configured to work on: release or release/*"
        echo ""
        read -p "Do you want to create a 'release' branch? (y/n): " -n 1 -r
        echo ""
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            git checkout -b release
            echo "Switched to 'release' branch"
        else
            echo "Aborted. Please switch to a release branch first."
            return 1
        fi
    fi

    # Check for uncommitted changes
    if [ -n "$(git status --porcelain)" ]; then
        echo "Warning: You have uncommitted changes."
        git status --short
        echo ""
        read -p "Do you want to continue anyway? (y/n): " -n 1 -r
        echo ""
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "Aborted. Please commit or stash your changes first."
            return 1
        fi
    fi

    # Determine what version will be created
    echo ""
    echo "Analyzing commits to determine next version..."
    NEXT_VERSION=$(poetry run semantic-release version --print 2>/dev/null || echo "")

    if [ -z "$NEXT_VERSION" ]; then
        echo "Error: Could not determine next version."
        echo "This might mean:"
        echo "  - No commits requiring a version bump since last release"
        echo "  - Branch is not properly configured in pyproject.toml"
        return 1
    fi

    echo "Next version will be: $NEXT_VERSION"
    echo ""

    # Ask for confirmation
    read -p "Do you want to proceed with release preparation for v$NEXT_VERSION? (y/n): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted by user."
        return 1
    fi

    # Run semantic-release
    echo ""
    echo "Running semantic-release to update version and changelog..."
    echo "This will:"
    echo "  - Update version in pyproject.toml"
    echo "  - Generate/update CHANGELOG.MD"
    echo "  - Create a local commit"
    echo "  - NOT create a git tag"
    echo "  - NOT push to remote"
    echo ""

    poetry run semantic-release version --no-tag --no-push --no-vcs-release

    # Check if it succeeded
    if [ $? -eq 0 ]; then
        echo ""
        echo "Release preparation completed successfully!"
        echo ""
        echo "Changes made:"
        git diff HEAD~1 --name-only
        echo ""
        echo "Next steps:"
        echo "  1. Review the changes: git diff HEAD~1"
        echo "  2. Push to your fork: git push origin $(git branch --show-current)"
        echo "  3. Create a PR to upstream/master with title: 'chore: release v$NEXT_VERSION'"
        echo "  4. After PR is merged, from clean master branch:"
        echo "     - git checkout master && git pull upstream master"
        echo "     - poetry build"
        echo "     - poetry publish"
    else
        echo ""
        echo "Error: semantic-release failed."
        echo "Check the error messages above for details."
        return 1
    fi
}

# Run the function
run_release_prep