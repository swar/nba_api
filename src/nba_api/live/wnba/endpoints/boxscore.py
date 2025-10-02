from nba_api.live.wnba.endpoints._base import Endpoint
from nba_api.live.wnba.library.http import WNBALiveHTTP


class BoxScore(Endpoint):
    endpoint_url = "boxscore/boxscore_{game_id}.json"
    expected_data = {
        "meta": {
            "version": 1,
            "code": 200,
            "request": "http://nba.cloud/games/1022500153/boxscore?Format=json",
            "time": "2025-07-24 23:07:22.884009"
        },
        "game": {
            "gameId": "1022500153",
            "gameTimeLocal": "2025-07-24T19:00:00-04:00",
            "gameTimeUTC": "2025-07-24T23:00:00Z",
            "gameTimeHome": "2025-07-24T19:00:00-04:00",
            "gameTimeAway": "2025-07-24T16:00:00-07:00",
            "gameEt": "2025-07-24T19:00:00-04:00",
            "duration": 121,
            "gameCode": "20250724/LVAIND",
            "gameStatusText": "Final",
            "gameStatus": 3,
            "regulationPeriods": 4,
            "period": 4,
            "gameClock": "PT00M00.00S",
            "attendance": 16166,
            "sellout": "0",
            "arena": {
                "arenaId": 1000063,
                "arenaName": "Gainbridge Fieldhouse",
                "arenaCity": "Indianapolis",
                "arenaState": "IN",
                "arenaCountry": "US",
                "arenaTimezone": "America/Indiana/Indianapolis"
            },
            "officials": [
                {
                    "personId": 101044,
                    "name": "Amy Bonner",
                    "nameI": "A. Bonner",
                    "firstName": "Amy",
                    "familyName": "Bonner",
                    "jerseyNum": "31",
                    "assignment": "OFFICIAL2"
                },
            ],
            "homeTeam": {
                "teamId": 1611661325,
                "teamName": "Fever",
                "teamCity": "Indiana",
                "teamTricode": "IND",
                "score": 80,
                "inBonus": "1",
                "timeoutsRemaining": 1,
                "periods": [
                    {
                        "period": 1,
                        "periodType": "REGULAR",
                        "score": 18
                    }
                ],
                "players": [
                    {
                        "status": "ACTIVE",
                        "order": 1,
                        "personId": 1629482,
                        "jerseyNum": "8",
                        "position": "SF",
                        "starter": "1",
                        "oncourt": "1",
                        "played": "1",
                        "statistics": {
                            "assists": 0,
                            "blocks": 0,
                            "blocksReceived": 0,
                            "fieldGoalsAttempted": 5,
                            "fieldGoalsMade": 4,
                            "fieldGoalsPercentage": 0.8,
                            "foulsOffensive": 0,
                            "foulsDrawn": 4,
                            "foulsPersonal": 2,
                            "foulsTechnical": 0,
                            "freeThrowsAttempted": 4,
                            "freeThrowsMade": 4,
                            "freeThrowsPercentage": 1.0,
                            "minus": 59.0,
                            "minutes": "PT32M55.00S",
                            "minutesCalculated": "PT33M",
                            "plus": 66.0,
                            "plusMinusPoints": 7.0,
                            "points": 15,
                            "pointsFastBreak": 2,
                            "pointsInThePaint": 2,
                            "pointsSecondChance": 0,
                            "reboundsDefensive": 3,
                            "reboundsOffensive": 0,
                            "reboundsTotal": 3,
                            "steals": 1,
                            "threePointersAttempted": 4,
                            "threePointersMade": 3,
                            "threePointersPercentage": 0.75,
                            "turnovers": 0,
                            "twoPointersAttempted": 1,
                            "twoPointersMade": 1,
                            "twoPointersPercentage": 1.0
                        },
                        "name": "Sophie Cunningham",
                        "nameI": "S. Cunningham",
                        "firstName": "Sophie",
                        "familyName": "Cunningham"
                    }
                ],
                "statistics": {
                    "assists": 17,
                    "assistsTurnoverRatio": 1.21428571428571,
                    "benchPoints": 4,
                    "biggestLead": 10,
                    "biggestLeadScore": "70-80",
                    "biggestScoringRun": 10,
                    "biggestScoringRunScore": "22-18",
                    "blocks": 1,
                    "blocksReceived": 3,
                    "fastBreakPointsAttempted": 5,
                    "fastBreakPointsMade": 1,
                    "fastBreakPointsPercentage": 0.2,
                    "fieldGoalsAttempted": 71,
                    "fieldGoalsEffectiveAdjusted": 0.485915492957746,
                    "fieldGoalsMade": 29,
                    "fieldGoalsPercentage": 0.408450704225352,
                    "foulsOffensive": 1,
                    "foulsDrawn": 21,
                    "foulsPersonal": 16,
                    "foulsTeam": 15,
                    "foulsTechnical": 0,
                    "foulsTeamTechnical": 2,
                    "freeThrowsAttempted": 14,
                    "freeThrowsMade": 11,
                    "freeThrowsPercentage": 0.785714285714286,
                    "leadChanges": 11,
                    "minutes": "PT200M00.00S",
                    "minutesCalculated": "PT200M",
                    "points": 80,
                    "pointsAgainst": 70,
                    "pointsFastBreak": 7,
                    "pointsFromTurnovers": 15,
                    "pointsInThePaint": 32,
                    "pointsInThePaintAttempted": 41,
                    "pointsInThePaintMade": 16,
                    "pointsInThePaintPercentage": 0.390243902439024,
                    "pointsSecondChance": 10,
                    "reboundsDefensive": 26,
                    "reboundsOffensive": 10,
                    "reboundsPersonal": 36,
                    "reboundsTeam": 10,
                    "reboundsTeamDefensive": 4,
                    "reboundsTeamOffensive": 6,
                    "reboundsTotal": 46,
                    "secondChancePointsAttempted": 12,
                    "secondChancePointsMade": 4,
                    "secondChancePointsPercentage": 0.333333333333333,
                    "steals": 9,
                    "teamFieldGoalAttempts": 0,
                    "threePointersAttempted": 23,
                    "threePointersMade": 11,
                    "threePointersPercentage": 0.478260869565217,
                    "timeLeading": "PT24M19.50S",
                    "timesTied": 5,
                    "trueShootingAttempts": 77.16,
                    "trueShootingPercentage": 0.5184033177812339,
                    "turnovers": 13,
                    "turnoversTeam": 1,
                    "turnoversTotal": 14,
                    "twoPointersAttempted": 48,
                    "twoPointersMade": 18,
                    "twoPointersPercentage": 0.375
                }
            },
            "awayTeam": {
                "teamId": 1611661319,
                "teamName": "Aces",
                "teamCity": "Las Vegas",
                "teamTricode": "LVA",
                "score": 70,
                "inBonus": "0",
                "timeoutsRemaining": 1,
                "periods": [
                    {
                        "period": 1,
                        "periodType": "REGULAR",
                        "score": 18
                    }
                ],
                "players": [
                    {
                        "status": "ACTIVE",
                        "order": 1,
                        "personId": 1629498,
                        "jerseyNum": "0",
                        "position": "SF",
                        "starter": "1",
                        "oncourt": "1",
                        "played": "1",
                        "statistics": {
                            "assists": 3,
                            "blocks": 0,
                            "blocksReceived": 0,
                            "fieldGoalsAttempted": 14,
                            "fieldGoalsMade": 8,
                            "fieldGoalsPercentage": 0.5714285714285711,
                            "foulsOffensive": 0,
                            "foulsDrawn": 1,
                            "foulsPersonal": 4,
                            "foulsTechnical": 0,
                            "freeThrowsAttempted": 2,
                            "freeThrowsMade": 2,
                            "freeThrowsPercentage": 1.0,
                            "minus": 66.0,
                            "minutes": "PT31M31.00S",
                            "minutesCalculated": "PT31M",
                            "plus": 65.0,
                            "plusMinusPoints": -1.0,
                            "points": 19,
                            "pointsFastBreak": 0,
                            "pointsInThePaint": 12,
                            "pointsSecondChance": 0,
                            "reboundsDefensive": 2,
                            "reboundsOffensive": 1,
                            "reboundsTotal": 3,
                            "steals": 1,
                            "threePointersAttempted": 4,
                            "threePointersMade": 1,
                            "threePointersPercentage": 0.25,
                            "turnovers": 1,
                            "twoPointersAttempted": 10,
                            "twoPointersMade": 7,
                            "twoPointersPercentage": 0.7
                        },
                        "name": "Jackie Young",
                        "nameI": "J. Young",
                        "firstName": "Jackie",
                        "familyName": "Young"
                    },
                ],
                "statistics": {
                    "assists": 12,
                    "assistsTurnoverRatio": 0.857142857142857,
                    "benchPoints": 4,
                    "biggestLead": 8,
                    "biggestLeadScore": "26-18",
                    "biggestScoringRun": 14,
                    "biggestScoringRunScore": "26-18",
                    "blocks": 3,
                    "blocksReceived": 1,
                    "fastBreakPointsAttempted": 9,
                    "fastBreakPointsMade": 1,
                    "fastBreakPointsPercentage": 0.111111111111111,
                    "fieldGoalsAttempted": 67,
                    "fieldGoalsEffectiveAdjusted": 0.417910447761194,
                    "fieldGoalsMade": 27,
                    "fieldGoalsPercentage": 0.402985074626866,
                    "foulsOffensive": 3,
                    "foulsDrawn": 16,
                    "foulsPersonal": 21,
                    "foulsTeam": 18,
                    "foulsTechnical": 0,
                    "foulsTeamTechnical": 0,
                    "freeThrowsAttempted": 17,
                    "freeThrowsMade": 14,
                    "freeThrowsPercentage": 0.823529411764706,
                    "leadChanges": 11,
                    "minutes": "PT200M00.00S",
                    "minutesCalculated": "PT200M",
                    "points": 70,
                    "pointsAgainst": 80,
                    "pointsFastBreak": 2,
                    "pointsFromTurnovers": 16,
                    "pointsInThePaint": 38,
                    "pointsInThePaintAttempted": 40,
                    "pointsInThePaintMade": 19,
                    "pointsInThePaintPercentage": 0.475,
                    "pointsSecondChance": 10,
                    "reboundsDefensive": 28,
                    "reboundsOffensive": 9,
                    "reboundsPersonal": 37,
                    "reboundsTeam": 5,
                    "reboundsTeamDefensive": 1,
                    "reboundsTeamOffensive": 4,
                    "reboundsTotal": 42,
                    "secondChancePointsAttempted": 8,
                    "secondChancePointsMade": 5,
                    "secondChancePointsPercentage": 0.625,
                    "steals": 7,
                    "teamFieldGoalAttempts": 0,
                    "threePointersAttempted": 15,
                    "threePointersMade": 2,
                    "threePointersPercentage": 0.133333333333333,
                    "timeLeading": "PT12M21.00S",
                    "timesTied": 5,
                    "trueShootingAttempts": 74.48,
                    "trueShootingPercentage": 0.469924812030075,
                    "turnovers": 14,
                    "turnoversTeam": 0,
                    "turnoversTotal": 14,
                    "twoPointersAttempted": 52,
                    "twoPointersMade": 25,
                    "twoPointersPercentage": 0.480769230769231
                }
            }
        }
    }

    arena = None
    away_team = None
    away_team_player_stats = None
    away_team_stats = None
    data_sets = None
    headers = None
    home_team = None
    home_team_player_stats = None
    home_team_stats = None
    game = None
    game_details = None
    nba_response = None
    officials = None

    def __init__(self, game_id, proxy=None, headers=None, timeout=30, get_request=True):
        self.game_id = game_id
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        if get_request:
            self.get_request()

    def get_request(self):
        self.nba_response = WNBALiveHTTP().send_api_request(
            endpoint=self.endpoint_url.format(game_id=self.game_id),
            parameters={},
            proxy=self.proxy,
            headers=self.headers,
            timeout=self.timeout,
        )
        self.load_response()

    def load_response(self):
        data_sets = self.nba_response.get_dict()
        if "game" in data_sets:
            self.game = Endpoint.DataSet(data=data_sets["game"])
            self.game_details = self.game.get_dict().copy()
            if "arena" in self.game.get_dict():
                self.arena = Endpoint.DataSet(data=data_sets["game"]["arena"])
                self.game_details.pop("arena")
            if "officials" in self.game.get_dict():
                self.officials = Endpoint.DataSet(data=data_sets["game"]["officials"])
                self.game_details.pop("officials")
            if "homeTeam" in self.game.get_dict():
                self.home_team = Endpoint.DataSet(data=data_sets["game"]["homeTeam"])

                # Home Team Player Stats
                self.home_team_player_stats = Endpoint.DataSet(
                    data=data_sets["game"]["homeTeam"]["players"]
                )

                # Home Team Stats
                home_team_stats = self.home_team.get_dict().copy()
                home_team_stats.pop("players")
                self.home_team_stats = Endpoint.DataSet(data=home_team_stats)

                self.game_details.pop("homeTeam")
            if "awayTeam" in self.game.get_dict():
                self.away_team = Endpoint.DataSet(data=data_sets["game"]["awayTeam"])

                # Away Team Player Stats
                self.away_team_player_stats = Endpoint.DataSet(
                    data=data_sets["game"]["awayTeam"]["players"]
                )

                # Away Team Stats
                away_team_stats = self.away_team.get_dict().copy()
                away_team_stats.pop("players")
                self.away_team_stats = Endpoint.DataSet(data=away_team_stats)

                self.game_details.pop("awayTeam")
            self.game_details = Endpoint.DataSet(data=self.game_details)
