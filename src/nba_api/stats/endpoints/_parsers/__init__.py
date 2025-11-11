"""
NBA Stats V3 endpoint parsers.

This package contains parsers for NBA Stats API V3 endpoints that return
complex nested JSON structures (as opposed to the simpler tabular format).

Each parser is responsible for:
- Extracting headers from the nested JSON structure
- Flattening nested data into tabular format
- Returning data in the format expected by Endpoint.DataSet
"""

from .boxscoreadvancedv3 import NBAStatsBoxscoreAdvancedV3Parser
from .boxscoredefensivev2 import NBAStatsBoxscoreDefensiveV2Parser
from .boxscorefourfactorsv3 import NBAStatsBoxscoreFourFactorsV3Parser
from .boxscorehustlev2 import NBAStatsBoxscoreHustleV2Parser
from .boxscorematchupsv3 import NBAStatsBoxscoreMatchupsParserV3
from .boxscoremiscv3 import NBAStatsBoxscoreMiscV3Parser
from .boxscoreplayertrackv3 import NBAStatsBoxscorePlayerTrackV3Parser
from .boxscorescoringv3 import NBAStatsBoxscoreScoringV3Parser
from .boxscoresummaryv3 import NBAStatsBoxscoreSummaryParserV3
from .boxscoretraditionalv3 import NBAStatsBoxscoreTraditionalParserV3
from .boxscoreusagev3 import NBAStatsBoxscoreUsageV3Parser
from .iststandings import NBAStatsISTStandingsParser
from .playbyplayv3 import NBAStatsPlayByPlayParserV3
from .scheduleleaguev2 import (
    NBAStatsScheduleLeagueV2IntParser,
    NBAStatsScheduleLeagueV2Parser,
)
from .scoreboardv3 import NBAStatsScoreboardV3Parser

__all__ = [
    "NBAStatsBoxscoreAdvancedV3Parser",
    "NBAStatsBoxscoreDefensiveV2Parser",
    "NBAStatsBoxscoreFourFactorsV3Parser",
    "NBAStatsBoxscoreHustleV2Parser",
    "NBAStatsBoxscoreMatchupsParserV3",
    "NBAStatsBoxscoreMiscV3Parser",
    "NBAStatsBoxscorePlayerTrackV3Parser",
    "NBAStatsBoxscoreScoringV3Parser",
    "NBAStatsBoxscoreSummaryParserV3",
    "NBAStatsBoxscoreTraditionalParserV3",
    "NBAStatsBoxscoreUsageV3Parser",
    "NBAStatsISTStandingsParser",
    "NBAStatsPlayByPlayParserV3",
    "NBAStatsScheduleLeagueV2Parser",
    "NBAStatsScheduleLeagueV2IntParser",
    "NBAStatsScoreboardV3Parser",
    "get_parser_for_endpoint",
]


# Mapping of endpoint names to their parser classes
_PARSER_REGISTRY = {
    "boxscoreadvancedv3": NBAStatsBoxscoreAdvancedV3Parser,
    "boxscoredefensivev2": NBAStatsBoxscoreDefensiveV2Parser,
    "boxscorefourfactorsv3": NBAStatsBoxscoreFourFactorsV3Parser,
    "boxscorehustlev2": NBAStatsBoxscoreHustleV2Parser,
    "boxscorematchupsv3": NBAStatsBoxscoreMatchupsParserV3,
    "boxscoremiscv3": NBAStatsBoxscoreMiscV3Parser,
    "boxscoreplayertrackv3": NBAStatsBoxscorePlayerTrackV3Parser,
    "boxscorescoringv3": NBAStatsBoxscoreScoringV3Parser,
    "boxscoresummaryv3": NBAStatsBoxscoreSummaryParserV3,
    "boxscoretraditionalv3": NBAStatsBoxscoreTraditionalParserV3,
    "boxscoreusagev3": NBAStatsBoxscoreUsageV3Parser,
    "playbyplayv3": NBAStatsPlayByPlayParserV3,
    "iststandings": NBAStatsISTStandingsParser,
    "scheduleleaguev2": NBAStatsScheduleLeagueV2Parser,
    "scheduleleaguev2int": NBAStatsScheduleLeagueV2IntParser,
    "scoreboardv3": NBAStatsScoreboardV3Parser,
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
