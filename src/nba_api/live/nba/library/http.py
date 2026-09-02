from nba_api.live.http import _COMMON_HEADERS, BaseLiveHTTP


class NBALiveHTTP(BaseLiveHTTP):
    base_url = "https://cdn.nba.com/static/json/liveData/{endpoint}"
    headers = {**_COMMON_HEADERS, "Host": "cdn.nba.com"}
