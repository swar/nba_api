import json

try:
    from pandas import DataFrame
    PANDAS = True
except ImportError:
    PANDAS = False


class Endpoint:

    class DataSet:
        key = None
        data = {}

        def __init__(self, data):
            self.data = data

        def get_json(self):
            return json.dumps(self.data)

        def get_dict(self):
            return self.data

        def get_data_frame(self):
            if not PANDAS:
                raise Exception('Import Missing - Failed to import DataFrame from pandas.')
            return DataFrame(self.data['data'], columns=self.data['headers'])

    def get_request_url(self):
        return self.nba_response.get_url()

    def get_available_data(self):
        return self.get_normalized_dict().keys()

    def get_response(self):
        return self.nba_response.get_response()

    def get_dict(self):
        return self.nba_response.get_dict()

    def get_json(self):
        return self.nba_response.get_json()

    def get_normalized_dict(self):
        return self.nba_response.get_normalized_dict()

    def get_normalized_json(self):
        return self.nba_response.get_normalized_json()

    def get_data_frames(self):
        return [data_set.get_data_frame() for data_set in self.data_sets]
