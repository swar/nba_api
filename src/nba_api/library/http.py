import json
import os
import random
from urllib.parse import quote_plus

import requests

try:
    from nba_api.library.debug.debug import DEBUG
except ImportError:
    DEBUG = False


try:
    from nba_api.library.debug.debug import DEBUG_STORAGE
except ImportError:
    DEBUG_STORAGE = False


try:
    from nba_api.library.debug.debug import PROXY
except ImportError:
    PROXY = ""


if DEBUG:
    from hashlib import md5

    print("DEBUG MODE")


class NBAResponse:
    def __init__(self, response: str, status_code: int | None, url: str | None) -> None:
        self._response = response
        self._status_code = status_code
        self._url = url
        self._dict_cache: dict | None = None
        self._json_cache: str | None = None

    def get_response(self) -> str:
        return self._response

    def get_dict(self) -> dict:
        if self._dict_cache is None:
            self._dict_cache = json.loads(self._response)
        return self._dict_cache

    def get_json(self) -> str:
        if self._json_cache is None:
            self._json_cache = json.dumps(self.get_dict())
        return self._json_cache

    def valid_json(self) -> bool:
        try:
            self.get_dict()
        except ValueError:
            return False
        return True

    def get_url(self) -> str | None:
        return self._url

    def get_status_code(self) -> int | None:
        return self._status_code


class NBAHTTP:
    nba_response: type[NBAResponse] = NBAResponse

    base_url: str | None = None

    parameters: tuple | None = None

    headers: dict[str, str] | None = None

    _session: requests.Session | None = None

    @classmethod
    def get_session(cls) -> requests.Session:
        session = cls._session
        if session is None:
            session = requests.Session()
            cls._session = session
        return session

    @classmethod
    def set_session(cls, session: requests.Session) -> None:
        cls._session = session

    def clean_contents(self, contents: str) -> str:
        return contents

    def send_api_request(
        self,
        endpoint: str,
        parameters: dict[str, str | None],
        referer: str | None = None,
        proxy: str | list[str] | None = None,
        headers: dict[str, str] | None = None,
        timeout: int | None = None,
        raise_exception_on_error: bool = False,
    ) -> NBAResponse:
        if not self.base_url:
            raise Exception("Cannot use send_api_request from _HTTP class.")
        base_url = self.base_url.format(endpoint=endpoint)
        endpoint = endpoint.lower()
        self.parameters = parameters

        if headers is not None:
            request_headers = headers
        elif referer:
            request_headers = {**self.headers, "Referer": referer}
        else:
            request_headers = self.headers

        if proxy is None:
            request_proxy = PROXY
        elif not proxy:
            request_proxy = None
        else:
            request_proxy = proxy

        if isinstance(request_proxy, list):
            request_proxy = random.choice(request_proxy)
            if DEBUG:
                print(request_proxy)

        proxies = None
        if request_proxy:
            proxies = {
                "http": request_proxy,
                "https": request_proxy,
            }

        url = None
        status_code = None
        contents = None
        file_path = None

        # tuples are faster to handle and iterate
        parameters = tuple(sorted(parameters.items(), key=lambda kv: kv[0]))

        if DEBUG and DEBUG_STORAGE:
            print(endpoint, parameters)
            directory_name = "debug_storage"
            parameter_string = "&".join(
                "{}={}".format(key, "" if val is None else quote_plus(str(val)))
                for key, val in parameters
            )
            url = f"{base_url}?{parameter_string}"
            print(url)
            file_name = "{}-{}.txt".format(
                endpoint, md5(parameter_string.encode("utf-8")).hexdigest()
            )
            file_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "debug", directory_name
            )
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            file_path = os.path.join(file_path, file_name)
            print(file_name, os.path.isfile(file_path))
            if os.path.isfile(file_path):
                with open(file_path) as f:
                    contents = f.read()
                status_code = 200
                print("loading from file...")

        if not contents:
            response = self.get_session().get(
                url=base_url,
                params=parameters,
                headers=request_headers,
                proxies=proxies,
                timeout=timeout,
            )
            url = response.url
            status_code = response.status_code
            contents = response.text

        contents = self.clean_contents(contents)
        if DEBUG and DEBUG_STORAGE:
            with open(file_path, "w") as f:
                f.write(contents)
            print(url)

        data = self.nba_response(response=contents, status_code=status_code, url=url)

        if raise_exception_on_error:
            if status_code is not None and status_code >= 400:
                raise Exception(
                    f"HTTPError: Request failed with status code {status_code}."
                )
            if not data.valid_json():
                raise Exception(
                    "InvalidResponse: Response is not in a valid JSON format."
                )

        return data
