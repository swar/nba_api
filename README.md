[![PyPi](https://img.shields.io/pypi/v/nba_api.svg?longCache=true&style=for-the-badge)](https://pypi.python.org/pypi/nba_api) [![PyPi](https://img.shields.io/pypi/l/nba_api.svg?longCache=true&style=for-the-badge)](https://pypi.python.org/pypi/nba_api)

# nba_api

##### Current Version: v1.0.3

`nba_api` is an API Client for `www.nba.com`. This package is meant to make the API Endpoints more accessible and to provide extensive documentation.

The APIs on `www.nba.com` are largely undocumented and changes frequently.

Please feel free to contribute and have an open discussion regarding improvements and additional APIs to be mapped.

#### Mapped API Clients

1. `stats.nba.com` - `stats`


## Installation
```commandline
pip install nba_api
```

## Required and Optional Packages

- [requests](http://www.python-requests.org/en/latest/)
- [pandas](https://pandas.pydata.org/) `optional`


## Usage Examples
- [`stats.nba.com`](https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/examples.md)


## Documentation

- [Table of Contents](https://github.com/swar/nba_api/tree/master/docs/table_of_contents.md)

- [Package Structure](https://github.com/swar/nba_api/tree/master/docs/package_structure.md)

- [Endpoint Analysis Format](https://github.com/swar/nba_api/tree/master/docs/endpoint_analysis_format.md)

- [Scripts](https://github.com/swar/nba_api/tree/master/docs/scripts.md)

- NBA API
    - Library
        - Debug 
            - [debug.py](https://github.com/swar/nba_api/tree/master/docs/nba_api/debug.md)
        - [http.py](https://github.com/swar/nba_api/tree/master/docs/nba_api/library/http.md)
    - Tools
        - [Endpoint Analysis](https://github.com/swar/nba_api/tree/master/docs/nba_api/tools/stats/endpoint_analysis/analysis.md)
        - [Endpoint Documentation Generator](https://github.com/swar/nba_api/tree/master/docs/nba_api/tools/stats/endpoint_documentation_generator/generator.md)
        - [Endpoint Py File Generator](https://github.com/swar/nba_api/tree/master/docs/nba_api/tools/stats/endpoint_py_file_generator/generator.md)
        - [Parameter Documentation Generator](https://github.com/swar/nba_api/tree/master/docs/nba_api/tools/stats/parameter_documentation_generator/generator.md)
    - Stats [`stats.nba.com`](https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/endpoints)
        - [Examples](https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/examples.md)
        - Library
            - [data.py](https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/library/data.md)
            - [http.py](https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/library/http.md)
            - [parameters.py](https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/library/parameters.md)
        - Static
            - [players.py](https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/static/players.md)
            - [teams.py](https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/static/teams.md)
        - [Endpoints](https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/endpoints_data_structure.md)