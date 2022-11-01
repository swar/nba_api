# Contributing to the NBA_API

Welcome, and thank you for your interest in contributing to the NBA_API!

There are many ways in which you can contribute, beyond writing code. The goal of this document is to provide a high-level overview of how you can get involved.

# Asking Questions

Have a question? Rather than opening an issue, head over to the [Slack](https://join.slack.com/t/nbaapi/shared_invite/zt-1ipsuai9j-GjZjuP9S2~Uczuny1t74zA) to connect with others, chat, and receive help.

# Reporting Issues

Have you identified a reproducible problem? Have a feature request? Identified a missing endpoint? Here's how you can make reporting your issue as effective as possible.

## Look For an Existing Issue

Before you create a new issue, please do a search in [open issues](https://github.com/swar/nba_api/issues) to see if the issue or feature request has already been filed.

If you find your issue already exists, make relevant comments and add your [reaction](https://github.com/blog/2119-add-reactions-to-pull-requests-issues-and-comments). Use a reaction in place of a "+1" comment:

* 👍 - upvote
* 👎 - downvote

If you cannot find an existing issue that describes your bug or feature, create a new issue using the guidelines below.

## Writing Good Bug Reports and Feature Requests

File a single issue per problem and feature request. Do not enumerate multiple bugs or feature requests in the same issue.

Do not add your issue as a comment to an existing issue unless it's for the identical input. Many issues look similar, but have different causes.

The more information you can provide, the more likely someone will be successful at reproducing the issue and finding a fix.

Please include the following with each issue:

* Version of the nba_api you are using

* Reproducible steps (1... 2... 3...) that cause the issue

* What you expected to occur, versus what you actually occur

* A code snippet that demonstrates the issue or a link to a code repository that can easily be pull down to recreate the issue locally

  * **Note:** Because the developers need to copy and paste the code snippet, including a code snippet as a media file (i.e. .gif) is not sufficient.

## Final Checklist

Please remember to do the following:

* [ ] Search the issue repository to ensure your report is a new issue

* [ ] Recreate the issue

* [ ] Simplify your code around the issue to better isolate the problem
<<<<<<< HEAD

# Contributing Code

The `nba_api` project has been setup in a way to support development across a wide range of operating systems including Linux, macOS, and Windows. Contributions are managed via GitHub [forks](https://docs.github.com/en/get-started/quickstart/fork-a-repo) and [pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

## Style Guidlines

* Code submitted should follow the style of the code already found throughout the repository.
* The structure of data returned to the consumer of the library should align with the data structures already found throughout the library.  
* Unit tests should accompany your code wherever possible
* Use `git rebase -i` to organize your commits ([Write Better Commits, Build Better Projects](https://github.blog/2022-06-30-write-better-commits-build-better-projects/))

### Collaborating on Open Source

#### Proposals

Should you wish to make a significant change within the project, please open a [GitHub Issue](https://github.com/swar/nba_api/issues) using the prefix `PROPOSAL:` within the subject.

#### Code Reviews

GitHub allows developers the ability to draft pull requestes. This is incredibly useful to get feedback early within the development cycle when making large or complex changes.

## Requirements

### Python Supported Versions

Supported versions can be found within the [build script](https://github.com/swar/nba_api/blob/master/.circleci/config.yml).

While `nba_api` makes every attempt to provide compatibility with [Supported Versions of Python](https://devguide.python.org/versions/), libraries that the `nba_api` depends on may not offer that same compatibility. Should this occur, the `nba_api` will support the next Supported Version of Python in which all libraries share mutual compatibility.

### Poetry

Development on `nba_api` requires [Poetry](https://python-poetry.org/docs/). Poetry provides [environment isolation](https://python-poetry.org/docs/managing-environments/) managing all dependencies and packaging in a deterministic way.

### pyenv (optional)

The `nba_api` project supports [pyenv](https://github.com/pyenv/pyenv) and includes a `poetry.lock` file to recognize the currently active environment.

```yaml
[virtualenvs]
prefer-active-python = true
```

## Setting up your environment

This guide assume familiarity with using GitHub and `git`.

### 1. Install and configure pyenv (optional)

Follow the [pyenv installation instructions](https://github.com/pyenv/pyenv).

### 2. Install Poetry

Follow the [Poetry installation instructions](https://python-poetry.org/docs/).

### 3. Fork the `nba_api`

Follow GitHub's instructions on how to [fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) a repository and [clone that repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository) for local development.

### 4. Using Poetry with `nba_api`

```python
# Create a isolated virtual environment inclusive of all dependencies
poetry install

# Once the environment has been created, active the environment for development
Poetry shell 
```

### 5. Validating Your Environment

Poetry provides all of the developer dependencies through the `pyproject.toml` file. This allows you to begin using the required development tools immediately.

```python
# Run Unit Test (all tests should pass)
pytest

# Validate for Style using Flake8 (only errors will be displayed)
flake8
```

### 6. When Complete, Open a PR

When you have completed your development and uploaded your changes to GitHub, [create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) to have your changes reviewed.
