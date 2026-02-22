"""Shared models for integration test catalogs."""


class EndpointSpec:
    """An endpoint class with pre-configured kwargs, ready to be called."""

    def __init__(self, endpoint_class, **kwargs):
        self.endpoint_class = endpoint_class
        self.kwargs = kwargs

    def __call__(self):
        return self.endpoint_class(**self.kwargs)
