import json
import numpy as np

try:
    from pandas import DataFrame, MultiIndex

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
                raise Exception(
                    "Import Missing - Failed to import DataFrame from pandas."
                )

            if "headers" not in self.data or not self.data["headers"]:
                return DataFrame()

            if isinstance(self.data['headers'][0], str):
                return DataFrame(self.data["data"], columns=self.data["headers"])

            else:  # Multiple levels of column names
                levels = []
                level_names = []
                for i in range(
                    len(self.data["headers"])
                ):  # Extend column names for level to full length
                    level = self.data["headers"][i]
                    level_names.append(
                        level["name"] if "name" in level else "LEVEL_" + str(i)
                    )
                    column_names = (
                        [""] * level["columnsToSkip"]
                        if "columnsToSkip" in level
                        else []
                    )
                    column_names += list(
                        np.repeat(
                            np.array(level["columnNames"]),
                            level["columnSpan"] if "columnSpan" in level else 1,
                        )
                    )
                    levels.append(column_names)
                midx = MultiIndex.from_arrays(
                    levels, names=level_names
                )  # Use MultiIndex for dataframe columns
                return DataFrame(self.data["data"], columns=midx)

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
