"""Proxy resolution and credential redaction for outgoing requests.

Everything here reads its inputs when called, never at import time, so tests and
callers can change the environment without reloading modules.

Precedence for the proxy used by a request:

1. the ``proxy`` argument (``""`` or ``False`` means "no proxy"; a list picks one at random)
2. the ``NBA_API_PROXY`` environment variable
3. ``PROXY`` in ``nba_api.library.debug.debug`` (legacy; emits a ``FutureWarning``)

Set ``NBA_API_REQUIRE_PROXY=1`` to make a request fail, before any socket is
opened, when none of the above yields a proxy. Live tests use this so they can
never reach NBA.com directly.
"""

import os
import random
import re
import warnings
from urllib.parse import quote, unquote

PROXY_ENV_VAR = "NBA_API_PROXY"
REQUIRE_PROXY_ENV_VAR = "NBA_API_REQUIRE_PROXY"

_TRUTHY = {"1", "true", "yes", "on"}
# Greedy to the last "@" in the token, so raw "/" or "@" in a password can't end the match early.
_USERINFO = re.compile(r"(?P<scheme>[a-zA-Z][a-zA-Z0-9+.-]*://)[^\s]*@")
_MIN_SECRET_LEN = 4


class ProxyRequiredError(RuntimeError):
    """A proxy is required (``NBA_API_REQUIRE_PROXY``) but none was configured."""


def _legacy_proxy():
    try:
        from nba_api.library.debug import debug
    except ImportError:
        return ""
    value = getattr(debug, "PROXY", "")
    if value:
        warnings.warn(
            "nba_api.library.debug.debug.PROXY is deprecated; set the "
            f"{PROXY_ENV_VAR} environment variable or pass proxy= instead.",
            FutureWarning,
            stacklevel=3,
        )
    return value


def proxy_required():
    return os.environ.get(REQUIRE_PROXY_ENV_VAR, "").strip().lower() in _TRUTHY


def resolve_proxy(proxy=None):
    """Return the proxy URL to use for one request, or ``None`` for a direct connection."""
    if proxy is None:
        chosen = os.environ.get(PROXY_ENV_VAR, "").strip() or _legacy_proxy()
    else:
        chosen = proxy

    if isinstance(chosen, (list, tuple)):
        # Drop blank entries so a stray "" can never make a request go out direct.
        candidates = [c.strip() for c in chosen if c and c.strip()]
        chosen = random.choice(candidates) if candidates else None
    elif isinstance(chosen, str):
        chosen = chosen.strip()

    chosen = chosen or None
    if chosen is None and proxy_required():
        raise ProxyRequiredError(
            f"{REQUIRE_PROXY_ENV_VAR} is set but no proxy is configured; "
            f"set {PROXY_ENV_VAR} (an explicit proxy='' does not bypass this)."
        )
    return chosen


def as_proxies(proxy_url):
    """Build the ``proxies`` mapping ``requests`` expects."""
    if not proxy_url:
        return None
    return {"http": proxy_url, "https": proxy_url}


def redact(text, proxy_url=None):
    """Mask proxy credentials in ``text``.

    With ``proxy_url``, masks that proxy's userinfo and password (raw,
    percent-decoded and percent-encoded) wherever they appear, and nothing else, so
    unrelated URLs in the message are left alone. Without it, masks the userinfo of
    any ``scheme://user:pass@`` URL.
    """
    text = str(text)
    if not proxy_url:
        # No proxy to compare against: mask the userinfo of any URL (used for log output).
        return _USERINFO.sub(r"\g<scheme>***@", text)
    if "@" in proxy_url:
        userinfo = proxy_url.partition("://")[2].rpartition("@")[0]
        password = userinfo.partition(":")[2]
        secrets = set()
        for value in (userinfo, password):
            secrets.update({value, unquote(value), quote(value, safe="")})
        # Longest first so a password is never half-masked by a shorter overlapping secret.
        for secret in sorted(secrets, key=len, reverse=True):
            if len(secret) >= _MIN_SECRET_LEN:
                text = text.replace(secret, "***")
    return text
