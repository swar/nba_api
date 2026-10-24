"""In-memory response cache, owned by one client.

Off by default. When on, it keeps the most recent ``size`` responses and drops the
least recently used one when full. Safe to share across threads.
"""

import threading
from collections import OrderedDict


class ResponseCache:
    def __init__(self, size=128):
        if isinstance(size, bool) or not isinstance(size, int) or size < 1:
            raise ValueError(f"cache_size must be a positive int, got {size!r}")
        self.size = size
        self._entries = OrderedDict()
        self._lock = threading.Lock()

    @staticmethod
    def key(site, endpoint, params):
        """Build a cache key from the site, endpoint name and query parameters."""
        return (site, endpoint, tuple(sorted(params.items())))

    def get(self, key):
        """Return the cached value for ``key``, or ``None`` if it isn't cached."""
        with self._lock:
            if key not in self._entries:
                return None
            self._entries.move_to_end(key)
            return self._entries[key]

    def set(self, key, value):
        with self._lock:
            self._entries[key] = value
            self._entries.move_to_end(key)
            if len(self._entries) > self.size:
                self._entries.popitem(last=False)

    def clear(self):
        with self._lock:
            self._entries.clear()

    def __len__(self):
        return len(self._entries)
