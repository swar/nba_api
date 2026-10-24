"""Build the public-signature snapshot of every exported endpoint class.

Run as a script, it prints the snapshot as JSON on stdout. The test runs it in a
fresh interpreter with ``datetime.now()`` frozen to ``FROZEN_NOW`` so that the
date-derived defaults in ``nba_api.stats.library.parameters`` (``Season.default``,
``SeasonYear.default``, ``GameDate.default``, ...) can be told apart from literal
defaults and written symbolically, e.g. ``season=Season.default``. The result
does not depend on the real date.

Date-derived attributes are found, not listed: ``parameters.py`` is loaded a
second time under ``PROBE_NOW`` and every class attribute whose value changed
is treated as date-derived.
"""

import datetime
import importlib.util
import inspect
import json
import sys

# Jan-Sep, so SeasonYear (year - 1) and WnbaSeasonYear (year) differ, and a year
# no endpoint uses as a literal default.
FROZEN_NOW = (1999, 2, 3)
PROBE_NOW = (2011, 11, 12)

_real_datetime = datetime.datetime


def _freeze(ymd):
    class FrozenDatetime(_real_datetime):
        @classmethod
        def now(cls, tz=None):
            return cls(*ymd, tzinfo=tz)

    datetime.datetime = FrozenDatetime


def _class_attrs(module):
    attrs = {}
    for cls_name, cls in vars(module).items():
        if not inspect.isclass(cls) or cls.__module__ != module.__name__:
            continue
        for attr in dir(cls):
            if attr.startswith("__"):
                continue
            value = getattr(cls, attr)
            if callable(value):
                continue
            owner = next(c for c in cls.__mro__ if attr in vars(c))
            attrs[(cls_name, attr)] = (value, owner.__name__)
    return attrs


def _date_derived_symbols(parameters):
    """Map (type name, frozen value) -> symbol for each date-derived attribute."""
    _freeze(PROBE_NOW)
    spec = importlib.util.spec_from_file_location(
        "_parameters_probe", parameters.__file__
    )
    probe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(probe)
    datetime.datetime = _real_datetime

    probe_attrs = _class_attrs(probe)
    candidates = {}
    for key, (value, owner) in _class_attrs(parameters).items():
        if probe_attrs[key][0] == value:
            continue
        symbol = f"{owner}.{key[1]}"
        candidates.setdefault((type(value).__name__, value), set()).add(symbol)

    symbols = {}
    for key, names in candidates.items():
        # Season.default and Season.current_season share a value: prefer "default".
        ranked = sorted(names, key=lambda s: (not s.endswith(".default"), s))
        if len(ranked) > 1 and ranked[1].endswith(".default"):
            raise RuntimeError(
                f"ambiguous date-derived defaults {ranked}; change FROZEN_NOW"
            )
        symbols[key] = ranked[0]
    return symbols


def _render_param(param, symbols):
    if param.kind is param.VAR_POSITIONAL:
        return f"*{param.name}"
    if param.kind is param.VAR_KEYWORD:
        return f"**{param.name}"
    if param.default is param.empty:
        return param.name
    default = param.default
    try:
        symbol = symbols.get((type(default).__name__, default))
    except TypeError:  # unhashable default
        symbol = None
    text = symbol or repr(default)
    if " at 0x" in text:
        raise RuntimeError(f"non-deterministic default for {param.name}: {text}")
    return f"{param.name}={text}"


def _describe(cls, symbols):
    params = []
    star_added = False
    for param in list(inspect.signature(cls.__init__).parameters.values())[1:]:
        if param.kind is param.KEYWORD_ONLY and not star_added:
            params.append("*")
        if param.kind in (param.KEYWORD_ONLY, param.VAR_POSITIONAL):
            star_added = True
        params.append(_render_param(param, symbols))
    entry = {
        "none_attrs": sorted(
            a for a in dir(cls) if not a.startswith("_") and getattr(cls, a) is None
        ),
        "params": params,
    }
    for attr in ("endpoint", "endpoint_url"):
        if attr in dir(cls):
            entry[attr] = getattr(cls, attr)
    if isinstance(getattr(cls, "expected_data", None), dict):
        entry["expected_data"] = sorted(cls.expected_data)
    return entry


def _exported(package, base):
    classes = {
        name: obj
        for name, obj in vars(package).items()
        if inspect.isclass(obj) and issubclass(obj, base) and obj is not base
    }
    modules = {cls.__module__.rsplit(".", 1)[1] for cls in classes.values()}
    if len(classes) != len(package.__all__) or modules != set(package.__all__):
        raise RuntimeError(
            f"{package.__name__}: {len(classes)} endpoint classes for "
            f"{len(package.__all__)} modules in __all__; expected one class per module"
        )
    return classes


def build_snapshot():
    _freeze(FROZEN_NOW)
    from nba_api.stats.library import parameters

    datetime.datetime = _real_datetime
    symbols = _date_derived_symbols(parameters)

    from nba_api.live.nba import endpoints as live_endpoints
    from nba_api.live.nba.endpoints._base import Endpoint as LiveEndpoint
    from nba_api.stats import endpoints as stats_endpoints
    from nba_api.stats.endpoints._base import Endpoint as StatsEndpoint

    snapshot = {}
    for prefix, package, base in (
        ("stats", stats_endpoints, StatsEndpoint),
        ("live", live_endpoints, LiveEndpoint),
    ):
        for name, cls in _exported(package, base).items():
            snapshot[f"{prefix}.{name}"] = _describe(cls, symbols)
    return snapshot


def dumps(snapshot):
    return json.dumps(snapshot, indent=2, sort_keys=True) + "\n"


if __name__ == "__main__":
    if "nba_api" in sys.modules:
        raise RuntimeError("run in a fresh interpreter")
    sys.stdout.write(dumps(build_snapshot()))
