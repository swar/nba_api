"""One response from an NBA site, with what was sent to get it."""

import json
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Response:
    site: str
    endpoint: str
    params: dict
    url: str  # proxy credentials already masked
    status: int
    fetched_at: datetime
    text: str

    def json(self):
        return json.loads(self.text)

    @property
    def ok(self):
        """True for a 200 whose body is valid JSON. Only these get cached."""
        if self.status != 200:
            return False
        try:
            self.json()
        except ValueError:
            return False
        return True
