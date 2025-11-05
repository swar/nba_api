"""
NBA Stats V3 endpoint parsers.

This package contains parsers for NBA Stats API V3 endpoints that return
complex nested JSON structures (as opposed to the simpler tabular format).

Each parser is responsible for:
- Extracting headers from the nested JSON structure
- Flattening nested data into tabular format
- Returning data in the format expected by Endpoint.DataSet
"""

from .boxscoreadvancedv3 import NBAStatsBoxscoreParserV3
from .boxscorematchupsv3 import NBAStatsBoxscoreMatchupsParserV3
from .boxscoresummaryv3 import NBAStatsBoxscoreSummaryParserV3
from .boxscoretraditionalv3 import NBAStatsBoxscoreTraditionalParserV3
from .iststandings import NBAStatsISTStandingsParser
from .playbyplayv3 import NBAStatsPlayByPlayParserV3
from .scheduleleaguev2 import (
    NBAStatsScheduleLeagueV2IntParser,
    NBAStatsScheduleLeagueV2Parser,
)

__all__ = [
    "NBAStatsBoxscoreParserV3",
    "NBAStatsBoxscoreTraditionalParserV3",
    "NBAStatsBoxscoreMatchupsParserV3",
    "NBAStatsBoxscoreSummaryParserV3",
    "NBAStatsPlayByPlayParserV3",
    "NBAStatsISTStandingsParser",
    "NBAStatsScheduleLeagueV2Parser",
    "NBAStatsScheduleLeagueV2IntParser",
]
