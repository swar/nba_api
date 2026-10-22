"""Pin date-derived season defaults to the season the VCR cassettes were recorded in.

``Season.default``, ``SeasonYear.default`` and ``SeasonID.default`` roll over to
the next season every October. The cassettes record requests for a fixed season,
so left alone every cassette-backed test would stop matching on Oct 1. Endpoint
parameters that default to one of those values are therefore pinned to the
recorded season instead.

When cassettes are re-recorded, bump ``RECORDED_SEASON_YEAR`` to the season they
were recorded in.
"""

import inspect

from nba_api.stats.library.parameters import Season, SeasonID, SeasonYear

RECORDED_SEASON_YEAR = 2025

# Date-derived default -> the value the cassettes were recorded with.
PINNED_SEASON_DEFAULTS = {
    Season.default: f"{RECORDED_SEASON_YEAR}-{str(RECORDED_SEASON_YEAR + 1)[2:]}",
    SeasonYear.default: RECORDED_SEASON_YEAR,
    SeasonID.default: f"2{RECORDED_SEASON_YEAR}",
}


def pinned_season_kwargs(endpoint_class, overrides=None):
    """Return kwargs pinning season params that use a date-derived default.

    Params listed in ``overrides`` are left alone so explicit values win.
    """
    overrides = overrides or {}
    pinned = {}
    for name, param in inspect.signature(endpoint_class.__init__).parameters.items():
        if name in overrides:
            continue
        default = param.default
        if isinstance(default, bool) or not isinstance(default, str | int):
            continue
        if default in PINNED_SEASON_DEFAULTS:
            pinned[name] = PINNED_SEASON_DEFAULTS[default]
    return pinned
