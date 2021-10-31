from nba_api.library import http


try:
    from nba_api.library.debug.debug import STATS_HEADERS
except ImportError:
    STATS_HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'cdn.nba.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    }


class NBALiveHTTP(http.NBAHTTP):

    nba_response = http.NBAResponse
    base_url = 'https://cdn.nba.com/static/json/liveData/{endpoint}'
    headers = STATS_HEADERS

    def clean_contents(self, contents):
        if '{"Message":"An error has occurred."}' in contents:
            return '<Error><Message>An error has occurred.</Message></Error>'
        return contents
