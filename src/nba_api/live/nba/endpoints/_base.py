import json


class Endpoint:
    class DataSet:
        key = None
        data = {}

        def __init__(self, data={}):
            self.data = data

        def get_json(self):
            return json.dumps(self.data)

        def get_dict(self):
            return self.data

    def get_request_url(self):
        return self.nba_response.get_url()

    def get_response(self):
        return self.nba_response.get_response()

    def get_dict(self):
        return self.nba_response.get_dict()

    def get_json(self):
        return self.nba_response.get_json()
