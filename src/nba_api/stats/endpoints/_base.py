import json
import numpy as np
from typing import Any, Dict, List, Optional, Union

try:
    from pandas import DataFrame, MultiIndex

    PANDAS = True
except ImportError:
    PANDAS = False
    DataFrame = Any
    MultiIndex = Any


class Endpoint:
    class DataSet:
        key: Optional[str] = None
        data: Dict[str, Any] = {}

        def __init__(self, data: Dict[str, Any]) -> None:
            self.data = data

        def get_json(self) -> str:
            """Return the data as a JSON string."""
            return json.dumps(self.data)

        def get_dict(self) -> Dict[str, Any]:
            """Return the data as a dictionary."""
            return self.data

        def get_data_frame(self) -> DataFrame:
            """Return the data as a pandas DataFrame.

            Raises:
                Exception: If pandas is not installed.
            """
            if not PANDAS:
                raise Exception(
                    "Import Missing - Failed to import DataFrame from pandas."
                )

            if "headers" not in self.data or not self.data["headers"]:
                return DataFrame()

            if isinstance(self.data["headers"][0], str):
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

    nba_response: Any = None
    data_sets: List[DataSet] = []

    def get_request_url(self) -> str:
        """Return the URL of the request."""
        return self.nba_response.get_url()

    def get_available_data(self) -> List[str]:
        """Return the keys of the available data sets."""
        return self.get_normalized_dict().keys()

    def get_response(self) -> str:
        """Return the raw response string."""
        return self.nba_response.get_response()

    def get_dict(self) -> Dict[str, Any]:
        """Return the response as a dictionary."""
        return self.nba_response.get_dict()

    def get_json(self) -> str:
        """Return the response as a JSON string."""
        return self.nba_response.get_json()

    def get_normalized_dict(self) -> Dict[str, Any]:
        """Return the response as a normalized dictionary."""
        return self.nba_response.get_normalized_dict()

    def get_normalized_json(self) -> str:
        """Return the response as a normalized JSON string."""
        return self.nba_response.get_normalized_json()

    def get_data_frames(self) -> List[DataFrame]:
        """Return a list of pandas DataFrames for all data sets."""
        return [data_set.get_data_frame() for data_set in self.data_sets]
