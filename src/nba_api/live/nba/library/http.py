from nba_api.live.http import BaseLiveHTTP, _COMMON_HEADERS


class NBALiveHTTP(BaseLiveHTTP):
    base_url = "https://cdn.nba.com/static/json/liveData/{endpoint}"
    headers = {**_COMMON_HEADERS, "Host": "cdn.nba.com"}
