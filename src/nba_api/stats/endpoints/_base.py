from __future__ import annotations

import json
from importlib.util import find_spec
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pandas import DataFrame

# pandas is imported on first use in get_data_frame(): importing it takes most of
# the time `import nba_api.stats.endpoints` costs, and get_dict() doesn't need it.
PANDAS = find_spec("pandas") is not None


class Endpoint:
    class DataSet:
        key: str | None = None
        data: dict[str, Any] = {}

        def __init__(self, data: dict[str, Any]) -> None:
            self.data = data

        def get_json(self) -> str:
            """Return the data as a JSON string."""
            return json.dumps(self.data)

        def get_dict(self) -> dict[str, Any]:
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

            from pandas import DataFrame, MultiIndex

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
                    column_names += [
                        name
                        for name in level["columnNames"]
                        for _ in range(level.get("columnSpan", 1))
                    ]
                    levels.append(column_names)
                midx = MultiIndex.from_arrays(
                    levels, names=level_names
                )  # Use MultiIndex for dataframe columns
                return DataFrame(self.data["data"], columns=midx)

    nba_response: Any = None
    data_sets: list[DataSet] = []

    def get_request_url(self) -> str:
        """Return the URL of the request."""
        return self.nba_response.get_url()

    def get_available_data(self) -> list[str]:
        """Return the keys of the available data sets."""
        return self.get_normalized_dict().keys()

    def get_response(self) -> str:
        """Return the raw response string."""
        return self.nba_response.get_response()

    def get_dict(self) -> dict[str, Any]:
        """Return the response as a dictionary."""
        return self.nba_response.get_dict()

    def get_json(self) -> str:
        """Return the response as a JSON string."""
        return self.nba_response.get_json()

    def get_normalized_dict(self) -> dict[str, Any]:
        """Return the response as a normalized dictionary."""
        return self.nba_response.get_normalized_dict()

    def get_normalized_json(self) -> str:
        """Return the response as a normalized JSON string."""
        return self.nba_response.get_normalized_json()

    def get_data_frames(self) -> list[DataFrame]:
        """Return a list of pandas DataFrames for all data sets."""
        return [data_set.get_data_frame() for data_set in self.data_sets]
