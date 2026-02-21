import json

import pytest

from nba_api.library.http import NBAHTTP, NBAResponse
from nba_api.live.nba.endpoints import odds
from nba_api.live.nba.library.http import NBALiveHTTP

# Mock odds response data
content = {
    "games": [
        {
            "gameId": "0022400913",
            "sr_id": "sr:match:52632103",
            "srMatchId": "52632103",
            "homeTeamId": "1610612745",
            "awayTeamId": "1610612740",
            "markets": [
                {
                    "name": "2way",
                    "odds_type_id": 1,
                    "group_name": "regular",
                    "books": [
                        {
                            "id": "sr:book:108",
                            "name": "Sportsbet",
                            "outcomes": [
                                {
                                    "odds_field_id": 1,
                                    "type": "home",
                                    "odds": "1.370",
                                    "opening_odds": "1.360",
                                    "odds_trend": "up",
                                },
                                {
                                    "odds_field_id": 2,
                                    "type": "away",
                                    "odds": "3.220",
                                    "opening_odds": "3.300",
                                    "odds_trend": "down",
                                },
                            ],
                            "url": "https://ad.doubleclick.net/ddm/clk/594881279;402977564;g;gdpr=${GDPR};gdpr_consent=${GDPR_CONSENT_755}",
                            "countryCode": "AUS",
                        },
                        {
                            "id": "sr:book:6565",
                            "name": "Novibet",
                            "outcomes": [
                                {
                                    "odds_field_id": 1,
                                    "type": "home",
                                    "odds": "1.370",
                                    "opening_odds": "1.340",
                                    "odds_trend": "up",
                                },
                                {
                                    "odds_field_id": 2,
                                    "type": "away",
                                    "odds": "3.200",
                                    "opening_odds": "3.250",
                                    "odds_trend": "down",
                                },
                            ],
                            "url": "https://www.novibet.gr/stoixima/mpasket/4372811/united-states/nba/5142827?btag=20045[\u00e2\u20ac\u00a6]ce=2004578_&utm_medium=affiliate&utm_campaign=STOIXIMAGENERIC",
                            "countryCode": "GR",
                        },
                        {
                            "id": "sr:book:6565",
                            "name": "Novibet",
                            "outcomes": [
                                {
                                    "odds_field_id": 1,
                                    "type": "home",
                                    "odds": "1.370",
                                    "opening_odds": "1.340",
                                    "odds_trend": "up",
                                },
                                {
                                    "odds_field_id": 2,
                                    "type": "away",
                                    "odds": "3.200",
                                    "opening_odds": "3.250",
                                    "odds_trend": "down",
                                },
                            ],
                            "url": "https://www.novibet.gr/stoixima/mpasket/4372811/united-states/nba/5142827?btag=20045[\u00e2\u20ac\u00a6]ce=2004578_&utm_medium=affiliate&utm_campaign=STOIXIMAGENERIC",
                            "countryCode": "CY",
                        },
                        {
                            "id": "sr:book:18186",
                            "name": "FanDuel",
                            "outcomes": [
                                {
                                    "odds_field_id": 1,
                                    "type": "home",
                                    "odds": "1.370",
                                    "opening_odds": "1.364",
                                    "odds_trend": "up",
                                },
                                {
                                    "odds_field_id": 2,
                                    "type": "away",
                                    "odds": "3.200",
                                    "opening_odds": "3.250",
                                    "odds_trend": "down",
                                },
                            ],
                            "url": "https://servedby.flashtalking.com/click/8/246790;8578295;369307;211;0/?ft_width=1&ft_heig[\u00e2\u20ac\u00a6]${GDPR_CONSENT_78}&us_privacy=${US_PRIVACY}&url=39466910",
                            "countryCode": "US",
                        },
                        {
                            "id": "sr:book:23879",
                            "name": "Olybet",
                            "outcomes": [
                                {
                                    "odds_field_id": 1,
                                    "type": "home",
                                    "odds": "3.050",
                                    "opening_odds": "1.500",
                                    "odds_trend": "up",
                                },
                                {
                                    "odds_field_id": 2,
                                    "type": "away",
                                    "odds": "1.350",
                                    "opening_odds": "2.500",
                                    "odds_trend": "down",
                                },
                            ],
                            "url": "https://www.olybet.eu/sports?competition=756&game=20426914&region=50003&type=0&sport=3&",
                            "countryCode": "EE",
                        },
                        {
                            "id": "sr:book:35226",
                            "name": "TabAustralia",
                            "outcomes": [
                                {
                                    "odds_field_id": 1,
                                    "type": "home",
                                    "odds": "1.370",
                                    "opening_odds": "1.300",
                                    "odds_trend": "up",
                                },
                                {
                                    "odds_field_id": 2,
                                    "type": "away",
                                    "odds": "3.200",
                                    "opening_odds": "3.700",
                                    "odds_trend": "down",
                                },
                            ],
                            "url": "https://www.tab.com.au/sports/betting/Basketball/competitions/NBA",
                            "countryCode": "AU",
                        },
                        {
                            "id": "sr:book:40165",
                            "name": "BetMGMCanadaOntario",
                            "outcomes": [
                                {
                                    "odds_field_id": 1,
                                    "type": "home",
                                    "odds": "1.351",
                                    "opening_odds": "1.308",
                                    "odds_trend": "up",
                                },
                                {
                                    "odds_field_id": 2,
                                    "type": "away",
                                    "odds": "3.250",
                                    "opening_odds": "3.600",
                                    "odds_trend": "down",
                                },
                            ],
                            "url": "https://sports.on.betmgm.ca/en/sports/basketball-7/betting/usa-9/nba-6004",
                            "countryCode": "CA",
                        },
                    ],
                },
                {
                    "name": "spread",
                    "odds_type_id": 4,
                    "group_name": "regular",
                    "books": [
                        {
                            "id": "sr:book:108",
                            "name": "Sportsbet",
                            "outcomes": [
                                {
                                    "odds_field_id": 10,
                                    "type": "home",
                                    "odds": "1.880",
                                    "opening_odds": "1.880",
                                    "odds_trend": "up",
                                    "spread": "-6.5",
                                    "opening_spread": -7.5,
                                },
                                {
                                    "odds_field_id": 12,
                                    "type": "away",
                                    "odds": "1.920",
                                    "opening_odds": "1.920",
                                    "odds_trend": "down",
                                    "spread": "6.5",
                                    "opening_spread": 7.5,
                                },
                            ],
                            "url": "https://ad.doubleclick.net/ddm/clk/594881279;402977564;g;gdpr=${GDPR};gdpr_consent=${GDPR_CONSENT_755}",
                            "countryCode": "AUS",
                        },
                        {
                            "id": "sr:book:5277",
                            "name": "Mozzartbet",
                            "outcomes": [
                                {
                                    "odds_field_id": 10,
                                    "type": "home",
                                    "odds": "1.900",
                                    "opening_odds": "1.900",
                                    "spread": "-7.5",
                                    "opening_spread": -8.5,
                                },
                                {
                                    "odds_field_id": 12,
                                    "type": "away",
                                    "odds": "1.900",
                                    "opening_odds": "1.900",
                                    "spread": "7.5",
                                    "opening_spread": 8.5,
                                },
                            ],
                            "url": "https://www.mozzartbet.com/sr/nba?utm_source=nba&utm_medium=mbet&utm_campaign=nba_match_schedule_mbet",
                            "countryCode": "RS",
                        },
                        {
                            "id": "sr:book:6565",
                            "name": "Novibet",
                            "outcomes": [
                                {
                                    "odds_field_id": 10,
                                    "type": "home",
                                    "odds": "1.820",
                                    "opening_odds": "1.850",
                                    "odds_trend": "up",
                                    "spread": "-6.5",
                                    "opening_spread": -7.5,
                                },
                                {
                                    "odds_field_id": 12,
                                    "type": "away",
                                    "odds": "1.980",
                                    "opening_odds": "1.850",
                                    "odds_trend": "down",
                                    "spread": "6.5",
                                    "opening_spread": 7.5,
                                },
                            ],
                            "url": "https://www.novibet.gr/stoixima/mpasket/4372811/united-states/nba/5142827?btag=20045[\u00e2\u20ac\u00a6]ce=2004578_&utm_medium=affiliate&utm_campaign=STOIXIMAGENERIC",
                            "countryCode": "GR",
                        },
                        {
                            "id": "sr:book:6565",
                            "name": "Novibet",
                            "outcomes": [
                                {
                                    "odds_field_id": 10,
                                    "type": "home",
                                    "odds": "1.820",
                                    "opening_odds": "1.850",
                                    "odds_trend": "up",
                                    "spread": "-6.5",
                                    "opening_spread": -7.5,
                                },
                                {
                                    "odds_field_id": 12,
                                    "type": "away",
                                    "odds": "1.980",
                                    "opening_odds": "1.850",
                                    "odds_trend": "down",
                                    "spread": "6.5",
                                    "opening_spread": 7.5,
                                },
                            ],
                            "url": "https://www.novibet.gr/stoixima/mpasket/4372811/united-states/nba/5142827?btag=20045[\u00e2\u20ac\u00a6]ce=2004578_&utm_medium=affiliate&utm_campaign=STOIXIMAGENERIC",
                            "countryCode": "CY",
                        },
                        {
                            "id": "sr:book:18186",
                            "name": "FanDuel",
                            "outcomes": [
                                {
                                    "odds_field_id": 10,
                                    "type": "home",
                                    "odds": "1.926",
                                    "opening_odds": "1.877",
                                    "spread": "-7",
                                    "opening_spread": -7.5,
                                },
                                {
                                    "odds_field_id": 12,
                                    "type": "away",
                                    "odds": "1.893",
                                    "opening_odds": "1.943",
                                    "spread": "7",
                                    "opening_spread": 7.5,
                                },
                            ],
                            "url": "https://servedby.flashtalking.com/click/8/246790;8578295;369307;211;0/?ft_width=1&ft_heig[\u00e2\u20ac\u00a6]${GDPR_CONSENT_78}&us_privacy=${US_PRIVACY}&url=39466910",
                            "countryCode": "US",
                        },
                        {
                            "id": "sr:book:35226",
                            "name": "TabAustralia",
                            "outcomes": [
                                {
                                    "odds_field_id": 10,
                                    "type": "home",
                                    "odds": "1.850",
                                    "opening_odds": "1.900",
                                    "odds_trend": "up",
                                    "spread": "-6.5",
                                    "opening_spread": -8,
                                },
                                {
                                    "odds_field_id": 12,
                                    "type": "away",
                                    "odds": "1.900",
                                    "opening_odds": "1.900",
                                    "odds_trend": "down",
                                    "spread": "6.5",
                                    "opening_spread": 8,
                                },
                            ],
                            "url": "https://www.tab.com.au/sports/betting/Basketball/competitions/NBA",
                            "countryCode": "AU",
                        },
                        {
                            "id": "sr:book:38812",
                            "name": "SportingbetBr",
                            "outcomes": [
                                {
                                    "odds_field_id": 10,
                                    "type": "home",
                                    "odds": "5.000",
                                    "opening_odds": "1.870",
                                    "odds_trend": "up",
                                    "spread": "-17.5",
                                    "opening_spread": -7.5,
                                },
                                {
                                    "odds_field_id": 12,
                                    "type": "away",
                                    "odds": "1.182",
                                    "opening_odds": "1.952",
                                    "odds_trend": "down",
                                    "spread": "17.5",
                                    "opening_spread": 7.5,
                                },
                            ],
                            "url": "https://sports.sportingbet.bet.br/?wm=5507762&utm_source=app-nba-voa&utm_campaign=linkdabioappnba2025&utm_content={{ad.id}}&utm_medium=appnba-{{campaign.id}}_{{adset.id}}_{{ad.id}}&utm_term=5507762-linkdabioappnba2025-sptbet-sprts-br-2025-1-2-pt-app--acq-app&tdpeh=fb-{{ad.id}}{{site_source_name}}{{placement}}",
                            "countryCode": "BR",
                        },
                        {
                            "id": "sr:book:40165",
                            "name": "BetMGMCanadaOntario",
                            "outcomes": [
                                {
                                    "odds_field_id": 10,
                                    "type": "home",
                                    "odds": "1.952",
                                    "opening_odds": "1.870",
                                    "odds_trend": "up",
                                    "spread": "-7.5",
                                    "opening_spread": -7.5,
                                },
                                {
                                    "odds_field_id": 12,
                                    "type": "away",
                                    "odds": "1.870",
                                    "opening_odds": "1.952",
                                    "odds_trend": "down",
                                    "spread": "7.5",
                                    "opening_spread": 7.5,
                                },
                            ],
                            "url": "https://sports.on.betmgm.ca/en/sports/basketball-7/betting/usa-9/nba-6004",
                            "countryCode": "CA",
                        },
                    ],
                },
            ],
        }
    ]
}


@pytest.fixture
def nba_http_patch(monkeypatch):
    class MockResponse:
        def __init__(*args, **kwargs):
            pass

        def send_api_request(
            self,
            endpoint,
            parameters,
            referer=None,
            proxy=None,
            headers=None,
            timeout=None,
            raise_exception_on_error=False,
        ):
            url = NBALiveHTTP.base_url.format(endpoint=endpoint)
            return NBAResponse(response=json.dumps(content), status_code=200, url=url)

    monkeypatch.setattr(NBAHTTP, "send_api_request", MockResponse.send_api_request)


def test_get_request_url():
    assert (
        odds.Odds().get_request_url()
        == "https://cdn.nba.com/static/json/liveData/odds/odds_todaysGames.json"
    )


def test_get_response(nba_http_patch):
    assert json.dumps(content) == odds.Odds().get_response()


def test_get_dict(nba_http_patch):
    assert odds.Odds().get_dict() == content


def test_games_dict(nba_http_patch):
    assert odds.Odds().games.get_dict() == content["games"]


def test_first_game_markets(nba_http_patch):
    games_data = odds.Odds().games.get_dict()
    assert games_data[0]["markets"] == content["games"][0]["markets"]


def test_first_game_book_outcomes(nba_http_patch):
    games_data = odds.Odds().games.get_dict()
    assert (
        games_data[0]["markets"][0]["books"][0]["outcomes"]
        == content["games"][0]["markets"][0]["books"][0]["outcomes"]
    )


def test_initialization_with_custom_headers():
    custom_headers = {"User-Agent": "Test"}
    odds_endpoint = odds.Odds(headers=custom_headers, get_request=False)
    assert odds_endpoint.headers == custom_headers


def test_initialization_with_custom_timeout():
    custom_timeout = 60
    odds_endpoint = odds.Odds(timeout=custom_timeout, get_request=False)
    assert odds_endpoint.timeout == custom_timeout


def test_initialization_with_proxy():
    proxy_url = "http://proxy.example.com"
    odds_endpoint = odds.Odds(proxy=proxy_url, get_request=False)
    assert odds_endpoint.proxy == proxy_url
