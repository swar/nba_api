from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP


class TeamDetails(Endpoint):
    endpoint = 'teamdetails'
    expected_data = {'TeamAwardsChampionships': ['YEARAWARDED', 'OPPOSITETEAM'], 'TeamAwardsConf': ['YEARAWARDED', 'OPPOSITETEAM'], 'TeamAwardsDiv': ['YEARAWARDED', 'OPPOSITETEAM'], 'TeamBackground': ['TEAM_ID', 'ABBREVIATION', 'NICKNAME', 'YEARFOUNDED', 'CITY', 'ARENA', 'ARENACAPACITY', 'OWNER', 'GENERALMANAGER', 'HEADCOACH', 'DLEAGUEAFFILIATION'], 'TeamHistory': ['TEAM_ID', 'CITY', 'NICKNAME', 'YEARFOUNDED', 'YEARACTIVETILL'], 'TeamHof': ['PLAYERID', 'PLAYER', 'POSITION', 'JERSEY', 'SEASONSWITHTEAM', 'YEAR'], 'TeamRetired': ['PLAYERID', 'PLAYER', 'POSITION', 'JERSEY', 'SEASONSWITHTEAM', 'YEAR'], 'TeamSocialSites': ['ACCOUNTTYPE', 'WEBSITE_LINK']}

    def __init__(self,
                 team_id):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'TeamID': team_id
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.team_awards_championships = Endpoint.DataSet(data=data_sets['TeamAwardsChampionships'])
        self.team_awards_conf = Endpoint.DataSet(data=data_sets['TeamAwardsConf'])
        self.team_awards_div = Endpoint.DataSet(data=data_sets['TeamAwardsDiv'])
        self.team_background = Endpoint.DataSet(data=data_sets['TeamBackground'])
        self.team_history = Endpoint.DataSet(data=data_sets['TeamHistory'])
        self.team_hof = Endpoint.DataSet(data=data_sets['TeamHof'])
        self.team_retired = Endpoint.DataSet(data=data_sets['TeamRetired'])
        self.team_social_sites = Endpoint.DataSet(data=data_sets['TeamSocialSites'])
