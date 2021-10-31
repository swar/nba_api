[![PyPI](https://img.shields.io/pypi/v/nba_api.svg?longCache=true&style=for-the-badge)](https://pypi.python.org/pypi/nba_api)
[![CircleCI (all branches)](https://img.shields.io/circleci/project/github/swar/nba_api.svg?style=for-the-badge)](https://circleci.com/gh/swar/nba_api) 
[![GitHub](https://img.shields.io/github/license/swar/nba_api.svg?style=for-the-badge)](https://pypi.python.org/pypi/nba_api)
[![GitHub](https://img.shields.io/pypi/dm/nba_api.svg?style=for-the-badge)](https://pepy.tech/project/nba-api)

# nba_api

#### An API Client package to access the APIs for NBA.com

##### Development Version: v1.1.10

`nba_api` is an API Client for `www.nba.com`. This package is meant to make the API Endpoints more accessible and to provide extensive documentation.

The APIs on `www.nba.com` are largely undocumented and change frequently.

Please feel free to contribute and have an open discussion regarding improvements and additional APIs to be mapped.


#### Recent Changes
* Adding individual proxy, headers, and timeout support for requests. [Usage](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/examples.md)


#### Mapped API Clients

1. `stats.nba.com` - `stats`


# Have Questions or Need Help?

Please try to avoid sending questions to my personal email that regard researching a solution to your specific problem. I don't mind helping, but the library has been setup with expansive documentation that should be checked first prior to reaching out to me personally. Alternatively, there are other places where you can ask for general advice that has been listed below.

## Slack Channel
There has been a public slack channel that has been setup for people to chat and receive help.
- https://join.slack.com/t/nbaapi/shared_invite/enQtOTY0MjIwMTI2ODIwLWIzZGFmMjQ4MDk4MTVmMTA2NWEwYmQzZDRiYTM3NDI4OWY5NGJiY2Q1M2EwZGUzOTQ1MTk4MDEyZGI1NGM2ZDI

## Stack Overflow
A tag has been set up for people to use when asking for help on Stack Overflow. Please tag posts with the `nba-api` tag.
- https://stackoverflow.com/questions/tagged/nba-api


# Use

## Installation
```commandline
pip install nba_api
```
Required and Optional Packages:
- [requests](https://requests.readthedocs.io/en/master/)
- [pandas](https://pandas.pydata.org/) (optional)


## Usage Examples
- [Basic Usage](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/examples.md) -- The basics of calling an API endpoint.
- [Jupyter Notebooks](https://github.com/swar/nba_api/tree/master/docs/examples) -- Larger practical examples in Jupyter Notebook format, including looking for play-by-play data for a particular game.

## Documentation

- [Table of Contents](https://github.com/swar/nba_api/tree/master/docs/table_of_contents.md)

- [Package Structure](https://github.com/swar/nba_api/tree/master/docs/package_structure.md)

- Stats
    - [Endpoints Documentation](/docs/nba_api/stats/endpoints)
    - Static
        - [players.py](https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/static/players.md)
        - [teams.py](https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/static/teams.md)


## Contributing and Development
### Development
To get started developing, clone the repo and `cd` into it.
Then, in an environment (conda or virtualenv) where you have not yet installed `nba_api`, run
```bash
python -m pip install -e .
```
This command will install the package for development, such that any changes you make in the repo will be reflected the next time you import the package in Python.

### Testing
If you make a change to the package, it's important to verify everything still works.
Do so by first installing the package for development, with the `-e` flag (see *Development* above), and then running
```bash
pytest
```
on the command line from the base directory of the repo.
The pytest utility will run through all the package tests and print output throughout, informing you of any failures.

### Contributing
We're always looking for people to help!
Some examples of ways to get involved are:
- fix a bug
- add a feature
- create or improve documentation and examples

Just fork this repo, make your changes (see [Development](#Development) above), and issue a pull request.

# Other

## Endpoint Analysis
A major purpose of this package is to map and analyze as many endpoints on NBA.com as possible. The documentation and analysis on the Endpoints and Parameters found in this package is some of the most extensive information available on these largely undocumented Endpoints. Please open an issue with any additional Endpoints/APIs. 

## Examples for Other Clients

[Endpoint Analysis JSON _for use with other clients_](https://github.com/swar/nba_api/tree/master/analysis_archive/stats)
