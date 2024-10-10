# NBA API Change Log

## About Versioning

- The NBA API uses [Semantic Versioning 2.0.0](https://semver.org/)
- Dates are [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant and formatted as `YYYY-MM-DD`

### Types of changes

- `Added` (new features)
- `Changed` (changes in existing functionality)
- `Deprecated` (soon-to-be removed functionality)
- `Removed` (removed functionality).
- `Fixed` (bug fixes)
- `Security` (vulnerabilities)
- `Contributor` (notes on updates to the project)

# Version History
## v1.6.0
Date: 2024.10.10

### Changed
* Updated .settings.json to recognize pytest tests
* Reformatted src/nba_api/stats/library/data.py for compliance with Flake8 rules
* Updated Static Player File

### Deprecated
* BoxScoreSimilarityScore (Person1Season & Person2Season no longer support valid values).
* Removed support for Python 3.8

### Fixed
* Fixed test for ShotChartLineupDetail.
* Fixed Bug #464 affecting Scoreboard & ScoreboardV2 endpoints

### Security
* Upgraded requests to ^2.32.3
* Upgraded certifi to ^2023.7.22 (CVE-2023-37920)
* Upgraded idna ^3.7.0 (CVE-2024-3651)

## v1.5.2
Date: 2024.08.28

### Fixed
* Fixed static data.py file where wnba_teams was missing.

## v1.5.1
Date: 2024.08.27

### Fixed
* Fix BoxScoreTraditionalV3 API Bug(some game stats starters and bench is None, cause 'NoneType' object has no attribute 'values') by @XatMassacrE in https://github.com/swar/nba_api/pull/458

### Changed
* Bump idna from 3.4 to 3.7 by @dependabot in https://github.com/swar/nba_api/pull/438
* Bump requests from 2.31.0 to 2.32.0 by @dependabot in https://github.com/swar/nba_api/pull/443
* Bump certifi from 2023.7.22 to 2024.7.4 by @dependabot in https://github.com/swar/nba_api/pull/454
* updated static players file by @rsforbes in https://github.com/swar/nba_api/pull/460

### Security
* updated requests to use version ^2.32.2 by @rsforbes in https://github.com/swar/nba_api/pull/459

**Full Changelog**: https://github.com/swar/nba_api/compare/v1.5.0...v1.5.1

## v1.5.0
### Added
- Add WNBA static data. by @cosmicac in https://github.com/swar/nba_api/pull/444
 
### Changed
- All NBA player and team static data current as of 2023.11.09 #398

### Fixed
- Update ScoreBoard game_date property name to score_board_date by @brooklynbagel in https://github.com/swar/nba_api/pull/422
- Update README.md (fixed Slack links) by @rsforbes in https://github.com/swar/nba_api/pull/424
- Update GameIDs Pattern Documentation by @TylerChasse in https://github.com/swar/nba_api/pull/437
- Updated docs with example output data by @shufinskiy in https://github.com/swar/nba_api/pull/447

## v1.4.1
### Changed
* Update documentation by @shufinskiy in https://github.com/swar/nba_api/pull/406

### Fixed
* boxscoremathups swapped places Def and Off columns names by @shufinskiy in https://github.com/swar/nba_api/pull/409

## v1.4.0
### Added
- In-Season Tournament Standings[ISTStandings](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/iststandings.md). @shufinskiy #396
- [EventMsgType](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/library/eventmsgtype.py) now contains INSTANT_REPLAY (18). @usharerose #384 
 
### Changed
- All NBA player and team static data current as of 2023.11.09 #398

### Deprecated
- [EventMsgType](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/library/eventmsgtype.py) UNKNOWN (18) has been deprecated and will be removed in a future release. #400

### Fixed
- The [playbyplay][https://github.com/rsforbes/nba_api/blob/master/src/nba_api/stats/library/playbyplayregex.py] regex for TURNOVER was updated to account for a space within the description provided by the NBA. #401

### Security
- Set minimum requirement for [certifi](https://pypi.org/project/certifi/) to 2023.7.22 per [CVE-2022-23491](https://www.cve.org/CVERecord?id=CVE-2023-37920) / [CWE-296](https://cwe.mitre.org/data/definitions/296.html) #384
- Bumped urllib3 from 2.0.6 to 2.0.7 @dependabot #388

### Developer Notes
- [Black](https://github.com/psf/black) has been implemented project wide and will be required for all PRs. #399
- DevContainer Changes #402
  - The VSCode DevContainer was updated to pin Debian-11 due to changes in Debian 12 that have impacted Python development. 
  - Poetry Shell now includes reference to the project.
  - the ms-python.flake and ms-python.vscode-pylance extensions are now included

## v1.3.1

Date: 2023.10.07

### Security
- Set minimum requirement for [requests](https://pypi.org/project/requests/) to 2.31 per [CVE-2023-32681](https://www.cve.org/CVERecord?id=CVE-2023-32681) / [CWE-200](https://cwe.mitre.org/data/definitions/200.html) 
- Set minimum requirement for [certifi](https://pypi.org/project/certifi/) to 2022.12.07 per [CVE-2022-23491](https://www.cve.org/CVERecord?id=CVE-2022-23491) / [CWE-345](https://cwe.mitre.org/data/definitions/345.html) 

## v1.3.0

Date: 2023-10-04

### Added

#### Endpoints
Eleven new endpoints were added to this release. A massive thank you to @shufinskiy.
- [BoxScoreAdvancedv3](docs/nba_api/stats/endpoints/boxscoreadvancedv3.md)
- [BoxScoreDefensivev2](docs/nba_api/stats/endpoints/boxscoredefensivev2.md)
- [BoxScoreFourFactorsv3](docs/nba_api/stats/endpoints/boxscorefourfactorsv3.md)
- [BoxScoreHustlev2](docs/nba_api/stats/endpoints/boxscorehustlev2.md)
- [BoxScoreMatchupsv3](docs/nba_api/stats/endpoints/boxscorematchupsv3.md)
- [BoxScoreMiscv3](docs/nba_api/stats/endpoints/boxscoremiscv3.md)
- [BoxScorePlayerTrackV3](docs/nba_api/stats/endpoints/boxscoreplayertrackv3.md)
- [BoxScoreScoringV3](docs/nba_api/stats/endpoints/boxscorescoringv3.md)
- [BoxScoreTraditionalv3](docs/nba_api/stats/endpoints/boxscoretraditionalv3.md)
- [BoxScoreUsagev3](docs/nba_api/stats/endpoints/boxscoreusagev3.md)
- [PlaybyPlayv3](docs/nba_api/stats/endpoints/playbyplayv3.md)

### Changed

#### NBA JSON schema 
Until recently, the NBA JSON schema followed a tabular strucutre exposing `headers` and `resultSet`. The NBA is now using a nested JSON schema. In addition, the data labels are no longer uppercase (e.g., `PCT_OREB`), are now camelcase and, in many cases, more descriptive (e.g., `percentageReboundsOffensive`).

#### Other
- All NBA player and team data has been updated to the date of this release.
- Corrected an invalid Slack within the text body to match the link present in the Slack shield.
- Updated NBA team data to include the Nuggets 2023 championship (#350)

## Known Issues
Due to the change in the NBA schema, the following methods will currently return and empty dataframe `{}`
- `.get_normalized_dict()`
- `.get_normalized_json()`
- `.get_headers_from_data_sets()`
All other calls are expected to work as expected.

### Removed
The following eleven endpoints have been deprecated by the NBA and subsequently removed from the library
- BoxScoreDefensive --> [BoxScoreDefensivev2](docs/nba_api/stats/endpoints/boxscoredefensivev2.md)
- BoxScoreMatchups --> [BoxScoreMatchupsv3](docs/nba_api/stats/endpoints/boxscorematchupsv3.md)
- LeagueHustleStatsPlayerLeaders --> unknown
- LeagueHustleStatsTeamLeaders --> unknown
- PlayerDashboardByOpponent --> unknown
- TeamDashboardByClutch --> unknown
- TeamDashboardByGameSplits --> unknown
- TeamDashboardByLastNGames --> unknown
- TeamDashboardByOpponent --> unknown
- TeamDashboardByTeamPerformance --> unknown
- TeamDashboardByYearOverYear --> unknown


### Security
- [urllib3](https://github.com/urllib3/urllib3) from 1.26.15 to 1.26.17. (#373) - @dependabot
- [certifi](https://github.com/certifi/python-certifi) from 2022.12.7 to 2023.7.22 (#360) - @dependabot

### Developer Tools
Updated dev container to dynamically set the python path for Poetry. (#369)

## v1.2.1

Date: 2023-06-13

### Security
- [requests](https://github.com/psf/requests) bumped from 2.28.2 to 2.31.0 via #344 - @dependabot

### Fixed

- Reverted alexfayad@5076fae050ec7d655af300cde7674756c4381943. Change broke materialized url and test. Original URL was found to be valid.
- Resolved bad url in documentation #322 - @alexfayad
- Fixed typo in causing src/nba_api/stats/endpoints/playerindex.py to fail #340 - @shufinskiy 
- Fixed expired Slack URL #347


### Developer Tools
- Support for VS Code Dev Containers (including auto-format via [black](https://github.com/psf/black))


## v1.2.0

Date: 2023-03-23

### Added

- Python: Support for 3.11 #331

- New Endpoint:
  - [PlayerIndex](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/playerindex.py) via #326 - @shufinskiy
  - [VideoDetailsAsset](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/videodetailsasset.py) via #325 - @OnerInce 

- Jupyter Notebooks (Binary Classification - Home Team Win-Loss Modeling) #329  - @TheResearchLab
  - [Home Team Win-Loss: Data Prep](https://github.com/swar/nba_api/blob/master/docs/examples/Home%20Team%20Win-Loss%20Modeling/Home%20Team%20Win-Loss%20Data%20Prep.ipynb)
  - [Home Team Win-Loss: Modeling](https://github.com/swar/nba_api/blob/master/docs/examples/Home%20Team%20Win-Loss%20Modeling/Home%20Team%20Win-Loss%20Modeling.ipynb)
  - Player Static Data: Updated as of 2023.03.23 #322

### Changed

- Removed Python max version release dependency to allow for all go-forward versions. Bugs with later Python versions can be addressed as needed. #331 

### Fixed

- Documentation: corrected parameter order on commonteamroster.md [PR#317](https://github.com/swar/nba_api/pull/317) - @JohannPally
- Corrected Hawks home state from Atlanta to Georgia #332
- Bug #327: Corrected a missing comma in `src/nba_api/stats/endpoints/__init__.py` #333

### Developer Tools

- Resolved CircleCI build where Poetry and CircleCI Docker images conflicted in how output is managed. #331 

## v1.1.14

Date: 2022-11-16

### Fixed

- Fixed a team turnover regular expression when working with PlayByPlay data.
- Endpoints
  - Fixed [PlayerGameLogs](https://github.com/FarhanSajid1/nba_api/blob/master/src/nba_api/stats/endpoints/playergamelogs.py) parameter OppTeamID --> OpponentTeamID ([#311](https://github.com/swar/nba_api/pull/311) - [FarhanSajid1](https://github.com/FarhanSajid1)

### Added

- [Poetry](https://python-poetry.org/): Python dependency management and packaging made easy
- Updated CONTRIBUTING.md on how to Contribute Code Using Poetry
- [Snyk](https://snyk.io/) for Security Scanning
- Exclusion to `.gitignore` for `.dccache` files created by Snyk CLI
- Introduced .flake8, resolve a number of style guide issues, added exclusions with future TODOs

### Changed

- Minimum Version for NumPy has been set to v1.22.22 due to a security vulnerability in [NumPy v1.21.6](https://security.snyk.io/package/pip/numpy/1.21.6)

### Removed

- Support for Python 3.7 due to a security vulnerability in [NumPy v1.21.6](https://security.snyk.io/package/pip/numpy/1.21.6)

### Security

- Upgraded NumPy from v1.21.6 to v1.22.2 due to three vulnerabilies:
  - [NULL Pointer Dereference](https://security.snyk.io/vuln/SNYK-PYTHON-NUMPY-2321964)
  - [Buffer Overflow](https://security.snyk.io/vuln/SNYK-PYTHON-NUMPY-2321966)
  - [Denial of Service (DOS)](https://security.snyk.io/vuln/SNYK-PYTHON-NUMPY-2321970)
- Integrated [DeepSource](https://deepsource.io/) for code security scanning

## v1.1.13

Date: 2022-10-16

### Fixed

Fix team_index_championship_year [#286](https://github.com/swar/nba_api/pull/286)

- add championship years to data-updater template
- re-add team_index_championship_year to static data
- add Bucks 2021 championship and GSW 2022

## v1.1.12

Date: 2022-10-11

### Added

- 2022-10-08 [Player Data]([https://github.com/swar/nba_api/blob/master/nba_api/stats/library/data.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/library/data.py))
- Endpoints
  - [VideoEventsAsset](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/videoeventsasset.py) ([#259](https://github.com/swar/nba_api/pull/259) - [prateekjaipuria](https://github.com/prateekjaipuria))
- [`CONTRIBUTING.MD`](https://github.com/swar/nba_api/blob/master/CONTRIBUTING.md)
- [`CHANGELOG.MD`](https://github.com/swar/nba_api/blob/master/CHANGELOG.md)
- GitHub issue template for bugs
- CircleCI build support for Python 3.10
- pyproject.toml ([PEP 621](https://peps.python.org/pep-0621/))

### Changed

- CircleCI
  - [Migrated to next-gen Convenience Images](https://circleci.com/docs/next-gen-migration-guide/)
  - [Config to Version 2.1](https://discuss.circleci.com/t/circleci-2-1-config-overview/26057)
  - Moved `flake8` and `pytest` into Commands
  - Parameterized docker images
- README.md
  - Link to [NBA.com Terms of Use](https://www.nba.com/termsofuse)
  - Getting started samples at the top
  - Other edits for improving the reading structure
- Project Structure
  - Source code moved from flat-layout to src-layout
  - Tests were divided into Unit/Integration

### Removed

- Support for Python 3.4, 3.5, and 3.6
- Setup.py file in favor of pyproject.toml ([PEP 621](https://peps.python.org/pep-0621/))

### Fixed

- [Issue #249](https://github.com/swar/nba_api/issues/249): `./nba_api/stats/endpoints/_base.py` requires `numpy` to format data for `get_data_frame`. `numpy` was not in the list of requirements, but is required.
- [Issue #278](https://github.com/swar/nba_api/issues/278): Fixed `playbyplayregex`, and included updated unit tests, where
  - The NBA removed a space that represented `distance` when `distance` was not included in the made/missed shot.
  - Jump Ball contained a single space in the description (regex now also supports multiple spaces empty description).
  - Team fouls no longer included Player/Referee, just the Team Name & Foul.

## v1.1.11

Date: 2021-11-8

- Merge pull request #231 from swar/live

## v1.1.10

Date: 2021.10-31

- Merge pull request #212 from baronet2/master
- Merge pull request #219 from edlavairee/find-teams-by-championship-year
- Merge pull request #226 from mjstamper/master
- Merge pull request #184 from rsforbes/live
- updated latest data.py from master
- changed prev_season to previous_season
- Merge pull request #1 from mjstamper/prev_season_add
- Added previous season to the Season parameter
- Merge pull request #225 from swar/static-data-update
- Added new feauture: User can now find the team who won a championship title for a given year.
- Added level names for MultiIndex columns of DataSet
- Add handling of multiple level column names in DataSets
- rolling back notebook changes
- removed .vscode/launch.json
- Updated Live Data Notebook
- undoing fix
- fixed references in tests for 3.4
- finilized testing and documentation for BoxScore
- Updated test for 3.4 & 3.5 backwards compatability
- Added AlwaysPresent to playbyplay.md
- Updated info on playbyplay.md
- major updates for live data (playbyplay, boxscore, and scoreboard)
- Merge pull request #7 from rsforbes/player_data_file
- Updated data.py with current player data
- Merge pull request #187 from rsforbes/playbyplay
- Merge pull request #188 from rsforbes/version_update
- Merge pull request #192 from rsforbes/gitignore_upd
- removed .vscode as it's in .gitignore and should have been checked in
- Adding Python 3.8 & 3.9 to the build
- further separated stats from live by moving over _base.py and having live endpoints reference that
- added fully working examples of live data in  docs/examples/PlayByPlay_Live.ipynb
- reverting nba_api/status/library/http.py to original
- updated live/endpoits/__init__.py to include new endpoints.
- updating live files for further review
- Fixed two issues. First, was not handling multiple in timeout_type. Second, new team violation type has been added by NBA.
- Live Data
- missed library for http.py
- adding in a new 'live' endpoint on s3 with libraries around playbyplay data. This will allow resutls during a live game

## v1.1.9

Date: 2020-01-27

- Updating table of content
- Adding test for LeagueDashOppPtShot
- Reverting more changes
- Changing to quotes
- Mistakenly pushed
- Merge pull request #152 from justinbt21/patch-1
- Adding 21 new endpoints with minor fixes to accommodate
- Removing TeamGameStreakFinder from tests
- Adding HustleStatsBoxScore endpoint
- Fixing link to requests
- Updates after re-run of analysis
- Updating documentation for analysis tool
- Printing proxy on DEBUG
- Upgrading endpoint analyzer
- Update __init__.py with LeagueDashOppPtShot
- Adding Questions and Help section

## v1.1.8

Date: 2020-01-27

- Forgot to remove debug code... this is why you don't program when you should be sleeping

## v1.1.7

- Forgot to add new endpoint on second section of __init__

## v1.1.6

- Updated Analysis
- Updated Endpoints and Parameter py files and docs
- Added Parameter Overriding
- Added new endpoint: TeamGameLogs
- Updating Static Player Data
- Updating error values
- Updating headers
- Adding proxy list support for randomization
- Merge pull request #115 from Mathiasme/patch-1
- typo

## v1.1.5

Date: 2019-11-09

- Adding new test: PlayerGameLogs
- Conforming to PEP8
- Conforming to PEP8
- Adding PlayerGameLogs to import
- Adding PlayerGameLogs
- Merge pull request #89 from rsforbes/master
- Updating static data
- Updating analysis.json
- Updating stats endpoint documentation
- Updating stats endpoints
- Updating parameters.md
- Adding new parameter mapping: MeasureTypePlayerGameLogs
- Adding new mappings for OppTeamID and MeasureType
- Adding new endpoints: PlayerGameLogs
- Changing is to == operator
- Updating Development Version
- Adding updated default headers
- Adding debug folder to gitignore
- Fixed bug where referee not included in playbyplay violation
- Fixed bug where referee did not appear in foul.
- Fixed the issue with Mark Morris in playbyplay using new variable
- simplified all playbyplay regex with the exception of pattern_turnover_player
- Fixed a but in playbyplay regex where Timeout now has 'Reg.' for Full Timeouts
- Merge pull request #82 from davidbobyang/master
- Fixed description in stats/library/http.md

## v1.1.4

Date: 2019-04-28

- Adding create static data file script
- Merge pull request #70 from rsforbes/master
- Merge pull request #67 from TK05/development/static-files-tools
- updated play by play tests, test data, and added new integration test to validate previous days play by play data.
- Update static players list
- Refactored tool to use existing endpoint

## v1.1.3

Date: 2019-04-21

- Merge remote-tracking branch 'origin/master'
- Removing tools folder from PyPi build
- Merge pull request #66 from TK05/development/active-players
- Merge pull request #65 from TK05/hotfix/py-generator
- Merge pull request #64 from rsforbes/master
- New tool to update static data
- Updated data doc with new feature
- Fixed typo
- Updated docs with new player features
- Added active status to static players list
- Fixed bug in py file generator
- Added PlayByPlay Ejection Regex. Moved test data out of test_playbyplayregex to conftest.py. Added additional regex unit tests. Moved tests into PlayByPlay folder
- Merge pull request #62 from TK05/master
- Cleaned up unnecessary leftovers

## v1.1.2

Date: v1.1.2

- Updating parameter mapping
- Updating deferred endpoint test list
- Updating stats endpoints
- Updating parameters documentation
- Updating endpoint documentation
- Updating analysis.json
- Merge branch 'TK05-develop/synergy' Merging with master
- Merge branch 'develop/synergy' of <https://github.com/TK05/nba_api> into TK05-develop/synergy Merging TK05-develop/synergy new endpoint
- Merge pull request #59 from rsforbes/master
- Added known parameters for SynergyPlayTypes endpoint
- Updated docs for SynergyPlayTypes endpoint
- Updated analysis.json with SynergyPlayTypes endpoint
- Added SynergyPlayTypes to tests
- Added SynergyPlayTypes endpoint with needed parameters
- Added endpoint and mappings for synergyplaytypes
- Removed errant import statment in test_playbyplayregex. Renamed TestPlayByPlay to TestPlayByPlayRegex.
- renamed EventMsgType.FREE_THROW_ATTEMPT to FREE_THROW
- Added ^ to regex beginning of pattern_free_throw. Included new eventmsgtype Enum
- Adding Tests to CircleCI
- Added support for VS Code w/ .gitignore update
- cleaned up playbyplay regex and added tests
- cleaned up playbyplay regex and added tests
- cleaned up playbyplayregex and included tests
- Merge branch 'master' of <https://github.com/swar/nba_api>
- Merge pull request #5 from rsforbes/dev
- Updated playbyplay_regex
- Merge pull request #55 from eswan18/pytest2
- Switch random wait generator from numpy to random
- Update readme to explain running tests
- Break endpoint tests into multiple files.
- Convert EndpointTester to class.
- Finish reorg of test_endpoints; make it work.
- Reorganized test_endpoints more.
- Update test_endpoints to be neater.

## v1.1.1

Date: 2019-04-07

- Reverting headers
- Updating README

## v1.1.0

Date: 2018-12-11

- Updating basic examples to show support for individual proxy, header, and timeout settings
- Updating endpoints with new analysis and template
- Updating documentation with new analysis
- Adding another missing required parameter
- Updating tests
- Updating analysis.json
- Adding more missing required parameters
- Updating headers
- Sorting parameters
- Sorting parameters
- Updating nullable parameter matches
- Updating parameter documentation
- Updating analysis.json
- Updating get_parameters method to return null on invalid json
- Updating with individual proxy, header, timeout, and url generation support
- Adding newly identified parameters
- Adding endpoints and new mappings
- Adding base changes for proxies, headers, timeouts, and url generation
- Updating with exceptions when missing any mappings
- Updating for endpoint changes and more nullable parameter tests
- Merge pull request #52 from rsforbes/master
- Merge pull request #4 from rsforbes/dev
- updated playbyplay_regex with .format() for backwards compatability
- Merge pull request #51 from rsforbes/master
- Merge pull request #3 from rsforbes/dev
- Revert "Added playbyplay data"
- including playbyplay_regex for playbyplay & playbyplayv2 VISITORDECRIPTION & HOMEDESCRIPTION fields
- Merge pull request #2 from rsforbes/dev
- Added playbyplay data
- Merge pull request #46 from eswan18/readme-dev-instr
- Update readme; add development instructions.
- Updating version log
- Updating development version
- Merge pull request #45 from eswan18/tabcomplete-endpoints
- Merge pull request #44 from rsforbes/master
- Make tab-complete work on nba_api.stats.endpoints.
- Cleaned up PlayByPlay book fixing Regex as well as fixed a bug in getting Home & Visitor Descriptions
- Merge pull request #39 from rsforbes/master
- Added Jupyter Play by Play Notebook
- Merge pull request #29 from Hoax5547/master
- Update teams.md
- Merge pull request #28 from Hoax5547/master
- Fixed description in teams.md
- Another minor formatting change for #19
- Updating Endpoint Documentation Generator with minor formatting changes for #19

## v1.0.7

Date: 2018-12-11

- Updating tests and DefenseHub doc
- Updating Endpoint Documentation Generator for #19
- Updating endpoints with new parameters from 2018-12-11 analysis json
- Updating documentation for #19
- Updating analysis archive to 2018-12-11
- Removing unnecessary doc
- Merge pull request #22 from eswan18/master
- moved examples link in readme to the Usage Examples heading
- moved examples to docs folder and updated readme
- slight cleanup of example notebooks
- adding examples folder

## v1.0.6 commit

Date: 2018-10-11

### Fixed

- Disabled DEBUG Mode that was enabled by default in v1.0.5

## v1.0.5 commit

Date: 2018-10-10

- Adding LeagueDashPtStats to tests and __init__
- Updating version log
- Switching default values
- Adding LeagueDashPtStats Endpoint
- Changing last_validated to last_validated_date
- Adding last validated date to analysis JSON
- Adding build badge, minor edits to badges
- Merge pull request #9 from cclauss/patch-1
- Typo
- Merge pull request #8 from cclauss/patch-1
- Drop legacy Python
- CircleCI: Add some automated testing

## v1.0.4

Date: 2018-09-25

    - Updating README urls

## v1.0.3

Date: 2018-09-25

- Updating stats examples
- README changes and removing index.md

## v1.0.2

Date: 2018-09-17

- Updating with PyCharm and Debug Files
- Escaping vertical bar character from endpoint documentation

## v1.0.1

Date: 2018-09-17

## v1.0.0

Date: 2018-09-16

- Initial commit
