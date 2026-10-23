"""What the repo already knows about an endpoint: cassettes, parsers, parameter enums.

Everything here is offline. It is compared against live responses in scope.py.
"""

import inspect
import json
import os
import re
from urllib.parse import parse_qsl, urlparse

from nba_api.stats.library import parameters as parameter_module

CASSETTE_DIRS = [
    os.path.join("tests", "integration", "smoke", "cassettes"),
    os.path.join("tests", "integration", "scenarios", "cassettes"),
]
# Date-like or open-ended params: enum discovery is meaningless for these.
SKIP_VALUE_DISCOVERY = {"Season", "SeasonYear", "SeasonID", "DateFrom", "DateTo"}
MAX_VALUES_PER_PARAMETER = 40
IGNORED_TOP_LEVEL = {"meta"}


def load_cassette(cls, endpoint):
    """Return (parameters, raw JSON) recorded for this endpoint, or (None, None)."""
    import yaml

    for directory in CASSETTE_DIRS:
        path = os.path.join(directory, f"test_endpoints[{cls.__name__}].yaml")
        if not os.path.exists(path):
            continue
        with open(path) as f:
            cassette = yaml.safe_load(f)
        for interaction in cassette.get("interactions", []):
            uri = urlparse(interaction["request"]["uri"])
            if uri.path.rstrip("/").split("/")[-1].lower() != endpoint:
                continue
            body = interaction["response"]["body"].get("string", "")
            try:
                raw = json.loads(body)
            except ValueError:
                continue
            return dict(parse_qsl(uri.query, keep_blank_values=True)), raw
    return None, None


def key_paths(value, prefix=""):
    """Every dict key path in a JSON value, with list elements merged as []."""
    paths = set()
    if isinstance(value, dict):
        for key, child in value.items():
            path = f"{prefix}.{key}" if prefix else key
            paths.add(path)
            paths |= key_paths(child, path)
    elif isinstance(value, list):
        for child in value:
            paths |= key_paths(child, f"{prefix}[]")
    return paths


def shape_diff(recorded, live):
    """Key paths added/removed between a recorded and a live response."""
    old, new = key_paths(recorded), key_paths(live)
    return {"added": sorted(new - old), "removed": sorted(old - new)}


def unparsed_fields(raw, data_sets):
    """Scalar fields in nested JSON that no dataset column surfaces.

    A leaf counts as surfaced if any column name contains it (parsers often
    prefix or suffix, e.g. personId -> personIdOff), case-insensitively. The
    response ``meta`` block is ignored. Treat the result as a lead, not proof.
    """
    columns = {str(c).lower() for headers in data_sets.values() for c in headers}
    leaves = {}
    for path in key_paths(raw):
        if path.split(".")[0] in IGNORED_TOP_LEVEL:
            continue
        leaf = path.rsplit(".", 1)[-1]
        if not any(leaf.lower() in column for column in columns):
            leaves.setdefault(leaf, path)
    # Only report scalars: containers are structure, not data.
    scalars = {}
    for leaf, path in leaves.items():
        if _is_scalar_path(raw, path):
            scalars[leaf] = path
    return dict(sorted(scalars.items()))


def _is_scalar_path(value, path):
    for part in re.split(r"\.", path):
        while isinstance(value, list):
            value = value[0] if value else None
        key = part.replace("[]", "")
        if not isinstance(value, dict) or key not in value:
            return False
        value = value[key]
    while isinstance(value, list):
        value = value[0] if value else None
    return not isinstance(value, dict | list)


def _public_classes():
    return {
        name: obj
        for name, obj in inspect.getmembers(parameter_module, inspect.isclass)
        if not name.startswith("_") and obj.__module__ == parameter_module.__name__
    }


def class_values(cls):
    values = set()
    for attr in dir(cls):
        if attr.startswith("_") or attr == "default":
            continue
        value = getattr(cls, attr)
        if isinstance(value, str | int) and not isinstance(value, bool):
            values.add(str(value))
    values.discard("")
    return values


def library_parameter_classes(endpoint_class):
    """Map NBA parameter name -> parameters.py class name used by the endpoint.

    Read from source: ``"PerMode": per_mode_detailed`` in ``self.parameters`` and
    ``per_mode_detailed=PerModeDetailed.default`` in the signature.
    """
    if endpoint_class is None:
        return {}
    source = inspect.getsource(endpoint_class.__init__)
    kwarg_class = dict(re.findall(r"(\w+)=(\w+)\.default", source))
    mapping = {}
    for name, kwarg in re.findall(r'"(\w+)":\s*(\w+)', source):
        if kwarg in kwarg_class:
            mapping[name] = kwarg_class[kwarg]
    return mapping


def parameter_family(parameter, library_class_name=None):
    """All parameters.py classes related to the one used for ``parameter``.

    The family is every class sharing the library class's most basic public
    ancestor, e.g. PerModeDetailed -> PerModeSimple and all its subclasses.
    Returns {class_name: values}.
    """
    classes = _public_classes()
    anchor = classes.get(library_class_name) or classes.get(parameter)
    if anchor is None:
        return {}
    public_bases = [c for c in anchor.__mro__ if c in classes.values()]
    root = public_bases[-1]
    family = {}
    for name, cls in classes.items():
        if issubclass(cls, root):
            values = class_values(cls)
            if values:
                family[name] = values
    return family


def summarize_values(parameter, family, library_class_name, accepted, rejected):
    """Turn accept/reject sets into a verdict about which class fits."""
    library_values = family.get(library_class_name, set())
    fitting = {n: v for n, v in family.items() if v <= accepted}
    exact = sorted(n for n, v in fitting.items() if v == accepted)
    best = exact or sorted(fitting, key=lambda n: (-len(fitting[n]), n))[:1]
    return {
        "library_class": library_class_name,
        "accepted": sorted(accepted),
        "rejected": sorted(rejected),
        "library_offers_rejected": sorted(library_values & rejected),
        "accepted_but_missing_from_library": sorted(accepted - library_values)
        if library_class_name
        else [],
        "best_fit_classes": best,
    }
