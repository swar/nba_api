# Security policy

## Supported versions

Security fixes are released for the latest version of `nba_api` on [PyPI](https://pypi.org/project/nba_api/). Please upgrade before reporting.

## Reporting a vulnerability

Please **do not** open a public issue for security problems.

Report them privately through [GitHub's private vulnerability reporting](https://github.com/swar/nba_api/security/advisories/new), or email swar.m.patel@gmail.com. Include the `nba_api` version, steps to reproduce, and the impact you expect.

You should get a reply within a week. Once a fix is released, the report is credited in the release notes unless you'd rather stay anonymous.

## Proxy credentials

`NBA_API_PROXY` and the `proxy=` argument may contain credentials. `nba_api` masks proxy URLs in request errors. If you find a case where a proxy URL or credential is logged, printed, or included in an exception, please report it as a vulnerability.
