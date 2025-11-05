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
    "get_parser_for_endpoint",
]


# Mapping of endpoint names to their parser classes
_PARSER_REGISTRY = {
    "boxscoreadvancedv3": NBAStatsBoxscoreParserV3,
    "boxscoredefensivev2": NBAStatsBoxscoreParserV3,
    "boxscorefourfactorsv3": NBAStatsBoxscoreParserV3,
    "boxscorehustlev2": NBAStatsBoxscoreParserV3,
    "boxscorematchupsv3": NBAStatsBoxscoreMatchupsParserV3,
    "boxscoremiscv3": NBAStatsBoxscoreParserV3,
    "boxscoreplayertrackv3": NBAStatsBoxscoreParserV3,
    "boxscorescoringv3": NBAStatsBoxscoreParserV3,
    "boxscoresummaryv3": NBAStatsBoxscoreSummaryParserV3,
    "boxscoretraditionalv3": NBAStatsBoxscoreTraditionalParserV3,
    "boxscoreusagev3": NBAStatsBoxscoreParserV3,
    "playbyplayv3": NBAStatsPlayByPlayParserV3,
    "iststandings": NBAStatsISTStandingsParser,
    "scheduleleaguev2": NBAStatsScheduleLeagueV2Parser,
    "scheduleleaguev2int": NBAStatsScheduleLeagueV2IntParser,
}


def get_parser_for_endpoint(endpoint, nba_dict):
    """
    Get the appropriate parser instance for a given endpoint.

    Args:
        endpoint (str): The endpoint name (e.g., "boxscoresummaryv3").
        nba_dict (dict): The raw API response dictionary.

    Returns:
        Parser instance configured with the provided data.

    Raises:
        KeyError: If the endpoint doesn't have a registered parser.
    """
    parser_class = _PARSER_REGISTRY[endpoint]
    return parser_class(nba_dict)
