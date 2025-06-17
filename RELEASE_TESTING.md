# Release Automation Testing Guide

This document explains how to test the automated release process without cutting actual production releases.

## Overview

The NBA API uses [semantic-release](https://semantic-release.gitbook.io/) for automated version management, changelog generation, and PyPI publishing. This automation is triggered by conventional commit messages when PRs are merged to the `master` branch.

## Testing Methods

### 1. Local Testing (Safest)

Since developers work on branches (not `master`), `semantic-release version --print` will always show "no release will be made". Here are better local testing methods:

```bash
# Install dependencies
poetry install

# Method 1: Analyze your conventional commits manually
# Check commits since last release that would trigger releases
git log --oneline --grep="feat\|fix\|BREAKING" $(git describe --tags --abbrev=0)..HEAD

# Determine release type from your commits:
# - Any "feat:" = minor version bump (1.10.0 → 1.11.0)
# - Any "fix:" = patch version bump (1.10.0 → 1.10.1)  
# - Any "feat!" or "BREAKING CHANGE:" = major version bump (1.10.0 → 2.0.0)
# - Only "docs:", "style:", "test:", "chore:", "build:" = no release

# Method 2: Validate commit message format
git log --oneline -10 | grep -E "^[a-f0-9]+ (feat|fix|docs|style|refactor|test|chore|build|ci)(\(.+\))?:"

# Method 3: Simulate on master branch (advanced)
git checkout master
git pull origin master
git merge --no-ff your_branch_name --no-commit
poetry run semantic-release version --print
git reset --hard HEAD  # Clean up
git checkout your_branch_name
```

**What this does:**
- Shows what type of release your commits would trigger
- Validates conventional commit format
- Tests actual semantic-release logic (Method 3)

### 2. Fork Testing (Recommended for Full Workflow)

For complete workflow testing following the standard fork workflow:

```bash
# 1. Fork the repository on GitHub (via GitHub UI)
# 2. Clone YOUR fork locally
git clone https://github.com/yourusername/nba_api.git
cd nba_api

# 3. Create test branch from your fork's master
git checkout -b your_branch_name

# 4. Make test commits using conventional format
git commit -m "feat: add test automation feature" --allow-empty
git commit -m "fix: resolve test issue" --allow-empty

# 5. Push test branch to your fork
git push origin your_branch_name

# 6. Create PR from your-fork/your_branch_name to upstream/master (via GitHub UI)
# 7. Merge the PR (this tests the automation on upstream)
# 8. After PR is merged, sync your fork's master:
git checkout master
git pull upstream master
git push origin master

# 9. Clean up test branch
git branch -D your_branch_name
git push origin --delete your_branch_name
```

**What this does:**
- Follows standard fork workflow (never develop on fork's master)
- Tests complete automation when PR merges to upstream/master
- No disruption to your fork's master branch
- Tests real workflow that contributors use

### 3. Commit Type Testing

Test different conventional commit types to see version impacts:

```bash
# Patch version bump (1.10.0 → 1.10.1)
git commit -m "fix: resolve timeout issue" --allow-empty

# Minor version bump (1.10.0 → 1.11.0)  
git commit -m "feat: add new endpoint support" --allow-empty

# Major version bump (1.10.0 → 2.0.0)
git commit -m "feat!: remove deprecated API" --allow-empty

# No release (documentation, style, etc.)
git commit -m "docs: update API documentation" --allow-empty
git commit -m "style: fix code formatting" --allow-empty
git commit -m "test: add unit tests" --allow-empty

# Check what version would be released
poetry run semantic-release version --print
```

## CircleCI Jobs

### Production Release Job (`release`)
- **Branch**: `master` only
- **Action**: Full automation (version, changelog, PyPI upload, GitHub release)
- **Trigger**: Merge to master with conventional commits
- **Environment**: Requires `PYPI_TOKEN` and optionally `GH_TOKEN`

## Environment Variables

For local testing, you don't need any special environment variables. For CircleCI testing:

- `PYPI_TOKEN` - Required for production releases (already configured)
- `GH_TOKEN` - Required for GitHub releases (configure if needed)

## Conventional Commit Format

The automation relies on [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Commit Types and Version Impact

| Type | Description | Version Bump | Example |
|------|-------------|--------------|---------|
| `feat` | New feature | Minor | `feat: add player stats endpoint` |
| `fix` | Bug fix | Patch | `fix: resolve timeout in HTTP requests` |
| `feat!` | Breaking change | Major | `feat!: remove deprecated endpoints` |
| `docs` | Documentation | None | `docs: update API examples` |
| `style` | Code style | None | `style: fix linting issues` |
| `refactor` | Code refactoring | None | `refactor: improve error handling` |
| `test` | Tests | None | `test: add integration tests` |
| `chore` | Maintenance | None | `chore: update dependencies` |

## Troubleshooting

### "no release will be made"
This message appears when:
- No conventional commits since last release
- Only commits that don't trigger releases (`docs`, `style`, etc.)
- Current branch isn't configured for releases

### Testing on Wrong Branch
Make sure you're on the correct branch:
- `master` - Production releases  
- Other branches - No release jobs run (testing should be done locally or on forks)

### Version Not Updating Locally
If local testing isn't showing expected results:
```bash
# Reset any local changes
git reset --hard HEAD

# Clean install dependencies
poetry install --no-ansi

# Use the manual commit analysis method instead
git log --oneline --grep="feat\|fix\|BREAKING" $(git describe --tags --abbrev=0)..HEAD
```

## Best Practices

1. **Always test locally first** using manual commit analysis
2. **Use fork workflow** for full workflow validation
3. **Follow conventional commit format** in your commits
4. **Clean up test branches** after testing
5. **Document any issues** you encounter during testing

## Example Test Workflow

```bash
# 1. Test locally first
git commit -m "feat: add new testing feature" --allow-empty
git commit -m "fix: resolve testing issue" --allow-empty

# 2. Check what would be released
poetry run semantic-release version --print
# Should show: 1.11.0 (minor bump for feat)

# 3. Test version bump without publishing
poetry run semantic-release version --no-push --no-vcs-release
# Updates local files to show what would happen

# 4. Reset changes and clean up
git reset --hard HEAD~2
# Removes test commits

# 5. For full workflow testing, use your fork:
# Fork repo → push changes → observe complete automation
```

This approach ensures safe testing without complex branch workflows or affecting production releases.