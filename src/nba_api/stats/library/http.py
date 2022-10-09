import json
from nba_api.library import http


try:
    from nba_api.library.debug.debug import STATS_HEADERS
except ImportError:
    STATS_HEADERS = {
        'Host': 'stats.nba.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'x-nba-stats-origin': 'stats',
        'x-nba-stats-token': 'true',
        'Connection': 'keep-alive',
        'Referer': 'https://stats.nba.com/',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }


class NBAStatsResponse(http.NBAResponse):

    def get_normalized_dict(self):
        raw_data = self.get_dict()

        data = {}

        if 'resultSets' in raw_data:
            results = raw_data['resultSets']
            if 'Meta' in results:
                return results
        else:
            results = raw_data['resultSet']
        if isinstance(results, dict):
            results = [results]
        for result in results:
            name = result['name']
            headers = result['headers']
            row_set = result['rowSet']

            rows = []
            for raw_row in row_set:
                row = {}
                for i in range(len(headers)):
                    row[headers[i]] = raw_row[i]
                rows.append(row)
            data[name] = rows

        return data

    def get_normalized_json(self):
        return json.dumps(self.get_normalized_dict())

    def get_parameters(self):
        if not self.valid_json() or 'parameters' not in self.get_dict():
            return None

        parameters = self.get_dict()['parameters']
        if isinstance(parameters, dict):
            return parameters

        parameters = {}
        for parameter in self.get_dict()['parameters']:
            for key, value in parameter.items():
                parameters.update({key: value})
        return parameters

    def get_headers_from_data_sets(self):
        raw_dict = self.get_dict()
        if 'resultSets' in raw_dict:
            results = raw_dict['resultSets']
        else:
            results = raw_dict['resultSet']
        if isinstance(results, dict):
            if 'name' not in results:
                return {}
            return {results['name']: results['headers']}
        return {result_set['name']: result_set['headers'] for result_set in results}

    def get_data_sets(self):
        raw_dict = self.get_dict()
        if 'resultSets' in raw_dict:
            results = raw_dict['resultSets']
        else:
            results = raw_dict['resultSet']
        if isinstance(results, dict):
            if 'name' not in results:
                return {}
            return {results['name']: {'headers': results['headers'], 'data': results['rowSet']}}
        return {result_set['name']: {'headers': result_set['headers'], 'data': result_set['rowSet']}
                for result_set in results}


class NBAStatsHTTP(http.NBAHTTP):

    nba_response = NBAStatsResponse

    base_url = 'https://stats.nba.com/stats/{endpoint}'

    headers = STATS_HEADERS

    def clean_contents(self, contents):
        if '{"Message":"An error has occurred."}' in contents:
            return '<Error><Message>An error has occurred.</Message></Error>'
        return contents
