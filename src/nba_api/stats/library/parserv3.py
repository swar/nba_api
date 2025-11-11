"""
DEPRECATED: This module has been moved to nba_api.stats.endpoints._parsers

The parsers have been split into individual files for better organization:
- boxscoreadvancedv3.py
- boxscoretraditionalv3.py
- boxscorematchupsv3.py
- boxscoresummaryv3.py
- playbyplayv3.py
- iststandings.py
- scheduleleaguev2.py

Please update your imports:
    OLD: from nba_api.stats.library.parserv3 import NBAStatsBoxscoreParserV3
    NEW: from nba_api.stats.endpoints._parsers import NBAStatsBoxscoreParserV3

Note: _parsers is private/internal. Do not import directly unless necessary.

This module will be removed in a future version.
"""

import warnings

# Re-export from new location for backward compatibility
from nba_api.stats.endpoints._parsers import (  # noqa: F401
    NBAStatsBoxscoreAdvancedV3Parser,
    NBAStatsBoxscoreMatchupsParserV3,
    NBAStatsBoxscoreSummaryParserV3,
    NBAStatsBoxscoreTraditionalParserV3,
    NBAStatsISTStandingsParser,
    NBAStatsPlayByPlayParserV3,
    NBAStatsScheduleLeagueV2IntParser,
    NBAStatsScheduleLeagueV2Parser,
    get_parser_for_endpoint,
)

# Legacy alias for backward compatibility
NBAStatsBoxscoreParserV3 = NBAStatsBoxscoreAdvancedV3Parser

warnings.warn(
    "nba_api.stats.library.parserv3 is deprecated. "
    "Use nba_api.stats.endpoints._parsers instead (internal API).",
    DeprecationWarning,
    stacklevel=2,
)
