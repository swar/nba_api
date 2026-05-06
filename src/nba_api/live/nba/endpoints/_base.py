import json
from typing import Any


class Endpoint:
    class DataSet:
        key: str | None = None

        def __init__(self, data: dict[str, Any] | list | None = None) -> None:
            if data is None:
                data = {}
            self.data = data

        def get_json(self) -> str:
            return json.dumps(self.data)

        def get_dict(self) -> dict[str, Any] | list:
            return self.data

    nba_response: Any = None
    data_sets: list[DataSet] | None = None

    def get_request_url(self) -> str:
        return self.nba_response.get_url()

    def get_response(self) -> str:
        return self.nba_response.get_response()

    def get_status_code(self) -> int:
        return self.nba_response.get_status_code()

    def get_dict(self) -> dict[str, Any]:
        return self.nba_response.get_dict()

    def get_json(self) -> str:
        return self.nba_response.get_json()
