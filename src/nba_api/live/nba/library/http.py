from nba_api.library import http

try:
    from nba_api.library.debug.debug import STATS_HEADERS
except ImportError:
    # Same browser profile as stats/library/http.py. cdn.nba.com returns 403
    # without the www.nba.com Referer, or for a Chrome User-Agent without the
    # matching Sec-Ch-Ua headers. Keep the Chrome version in sync with the stats
    # headers when bumping it.
    STATS_HEADERS = {
        "Host": "cdn.nba.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Referer": "https://www.nba.com/",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Sec-Ch-Ua": '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Fetch-Dest": "empty",
    }


class NBALiveHTTP(http.NBAHTTP):
    nba_response = http.NBAResponse
    base_url = "https://cdn.nba.com/static/json/liveData/{endpoint}"
    headers = STATS_HEADERS

    def clean_contents(self, contents):
        if '{"Message":"An error has occurred."}' in contents:
            return "<Error><Message>An error has occurred.</Message></Error>"
        return contents
