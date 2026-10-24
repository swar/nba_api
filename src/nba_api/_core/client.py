"""The 2.0 client. Only cache settings so far; more options get added as they are decided."""

from nba_api._core.cache import ResponseCache

_UNSET = object()


class Client:
    def __init__(self, cache=False, cache_size=_UNSET):
        if not isinstance(cache, bool):
            raise TypeError(f"cache must be True or False, got {cache!r}")
        if cache_size is not _UNSET and not cache:
            raise ValueError("cache_size was set but cache is off; pass cache=True")
        self.cache = (
            ResponseCache(128 if cache_size is _UNSET else cache_size)
            if cache
            else None
        )
