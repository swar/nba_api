"""Shared models for integration test helpers."""

import inspect

from .constants import INFRASTRUCTURE_PARAMS, PARAM_DEFAULTS


class EndpointSpec:
    """An endpoint class with pre-configured kwargs, ready to be called.

    Required parameters (those with no default in ``__init__``) are resolved
    automatically from ``PARAM_DEFAULTS``. Optional parameters use the endpoint's
    own defaults unless explicitly overridden here.

    Any kwargs passed at construction time override ``PARAM_DEFAULTS``.
    """

    def __init__(self, endpoint_class, deprecated=None, skip=None, **overrides):
        self.endpoint_class = endpoint_class
        self.deprecated = deprecated
        self.skip = skip
        self.overrides = overrides
        self.kwargs = overrides

    def __call__(self):
        sig = inspect.signature(self.endpoint_class.__init__)
        resolved = {}
        unresolved = []

        for name, param in sig.parameters.items():
            if name == "self" or name in INFRASTRUCTURE_PARAMS:
                continue
            if param.kind in (
                inspect.Parameter.VAR_POSITIONAL,
                inspect.Parameter.VAR_KEYWORD,
            ):
                continue
            if param.default is inspect.Parameter.empty:
                if name in self.overrides:
                    resolved[name] = self.overrides[name]
                elif name in PARAM_DEFAULTS:
                    resolved[name] = PARAM_DEFAULTS[name]
                else:
                    unresolved.append(name)

        if unresolved:
            raise ValueError(
                f"{self.endpoint_class.__name__} has required params not in "
                f"PARAM_DEFAULTS and no override was provided: {unresolved}. "
                f"Add them to PARAM_DEFAULTS in constants.py or pass them as "
                f"overrides to EndpointSpec."
            )

        return self.endpoint_class(**{**resolved, **self.overrides})
