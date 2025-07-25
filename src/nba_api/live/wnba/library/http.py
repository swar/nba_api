from nba_api.live.http import BaseLiveHTTP, _COMMON_HEADERS


class WNBALiveHTTP(BaseLiveHTTP):
    base_url = "https://cdn.wnba.com/static/json/liveData/{endpoint}"
    headers = {**_COMMON_HEADERS, "Host": "cdn.wnba.com"}
