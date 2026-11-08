"""Errors raised by the 2.0 core. ``except NBAAPIError`` catches all of them.

Each error that got a reply carries it as ``.response`` (a Response, proxy already
masked). Network errors also subclass the matching ``requests`` exception, so
``except requests.Timeout`` keeps working.
"""

import requests


class NBAAPIError(Exception):
    def __init__(self, message, response=None):
        super().__init__(message)
        self.response = response


class TransportError(NBAAPIError, requests.RequestException):
    """The request never got a reply: timeout, connection failure or reset."""


class ProxyError(TransportError, requests.exceptions.ProxyError):
    """The proxy failed: wrong credentials, unreachable, or it refused the request."""


# Private so the public names stay few; each still counts as TransportError and as
# the requests exception it replaces.
class _ConnectTimeout(TransportError, requests.ConnectTimeout):
    pass


class _ReadTimeout(TransportError, requests.ReadTimeout):
    pass


class _ConnectionError(TransportError, requests.ConnectionError):
    pass


class BlockedError(NBAAPIError):
    """NBA's CDN (Akamai) served a block page instead of data."""


class ParameterError(NBAAPIError):
    """NBA rejected one or more parameters (HTTP 400)."""

    def __init__(self, message, response=None, fields=None):
        super().__init__(message, response)
        self.fields = fields or {}


class HTTPStatusError(NBAAPIError):
    """NBA replied with a non-200 status not covered by a more specific error."""


class NotFoundError(NBAAPIError):
    """The endpoint, or the live file for a game, doesn't exist."""


class InvalidResponseError(NBAAPIError):
    """NBA replied 200 but the body isn't usable JSON."""
