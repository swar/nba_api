"""NBA Stats HTTP client and response handling."""

import json

from nba_api.library import http

try:
    from nba_api.library.debug.debug import STATS_HEADERS
except ImportError:
    STATS_HEADERS = {
        "Host": "stats.nba.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Referer": "https://stats.nba.com/",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Sec-Ch-Ua": '"Chromium";v="140", "Google Chrome";v="140", "Not;A=Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Fetch-Dest": "empty",
    }


class NBAStatsResponse(http.NBAResponse):
    """Response handler for NBA Stats API requests."""

    def get_normalized_dict(self):
        raw_data = self.get_dict()

        data = {}

        legacy_headers = ["resultSets", "resultSet"]
        is_legacy = set(legacy_headers) & set(raw_data.keys())

        if is_legacy:
            if "resultSets" in raw_data:
                results = raw_data["resultSets"]
                if "Meta" in results:
                    return results
            else:
                results = raw_data["resultSet"]
            if isinstance(results, dict):
                results = [results]
            for result in results:
                name = result["name"]
                headers = result["headers"]
                row_set = result["rowSet"]

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
        if not self.valid_json() or "parameters" not in self.get_dict():
            return None

        parameters = self.get_dict()["parameters"]
        if isinstance(parameters, dict):
            return parameters

        parameters = {}
        for parameter in self.get_dict()["parameters"]:
            for key, value in parameter.items():
                parameters.update({key: value})
        return parameters

    def get_headers_from_data_sets(self):
        raw_dict = self.get_dict()

        legacy_headers = ["resultSets", "resultSet"]
        is_legacy = set(legacy_headers) & set(raw_dict.keys())
        if not is_legacy:
            return {}

        if "resultSets" in raw_dict:
            results = raw_dict["resultSets"]
        else:
            results = raw_dict["resultSet"]
        if isinstance(results, dict):
            if "name" not in results:
                return {}
            return {results["name"]: results["headers"]}
        return {result_set["name"]: result_set["headers"] for result_set in results}

    def get_data_sets(self, endpoint=None):
        raw_dict = self.get_dict()

        if endpoint is None:
            # Process Tabular Json
            if "resultSets" in raw_dict:
                results = raw_dict["resultSets"]
            else:
                results = raw_dict["resultSet"]
            if isinstance(results, dict):
                if "name" not in results:
                    return {}
                return {
                    results["name"]: {
                        "headers": results["headers"],
                        "data": results["rowSet"],
                    }
                }
            return {
                result_set["name"]: {
                    "headers": result_set["headers"],
                    "data": result_set["rowSet"],
                }
                for result_set in results
            }
        else:
            # Process V3 endpoint with custom parser
            # Lazy import to avoid circular dependency
            from nba_api.stats.endpoints._parsers import get_parser_for_endpoint

            endpoint_parser = get_parser_for_endpoint(endpoint, self.get_dict())
            return endpoint_parser.get_data_sets()


class NBAStatsHTTP(http.NBAHTTP):
    """HTTP client for NBA Stats API with custom response handling."""

    nba_response = NBAStatsResponse

    base_url = "https://stats.nba.com/stats/{endpoint}"

    headers = STATS_HEADERS

    def clean_contents(self, contents):
        if '{"Message":"An error has occurred."}' in contents:
            return "<Error><Message>An error has occurred.</Message></Error>"
        return contents
