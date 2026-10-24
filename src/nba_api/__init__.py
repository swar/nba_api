name = "nba_api"


def __getattr__(attr):
    # __version__ is looked up on first access: importing importlib.metadata takes
    # most of the time a bare `import nba_api` costs.
    if attr == "__version__":
        from importlib.metadata import version

        global __version__
        __version__ = version("nba_api")
        return __version__
    raise AttributeError(f"module {__name__!r} has no attribute {attr!r}")
