import os
import json
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
    PROXY = ''


if DEBUG:
    from hashlib import md5
    print('DEBUG MODE')


class NBAResponse:
    def __init__(self, response, url):
        self._response = response
        self._url = url

    def get_response(self):
        return self._response

    def get_dict(self):
        return json.loads(self._response) if self._response else {'error': 'Response is None'}

    def get_json(self):
        return json.dumps(self.get_dict())

    def valid_json(self):
        try:
            self.get_dict()
        except ValueError:
            return False
        return True

    def get_url(self):
        return self._url


class NBAHTTP:

    nba_response = NBAResponse

    base_url = None

    headers = None

    def clean_contents(self, contents):
        return contents

    def send_api_request(self, endpoint, parameters, referer=None, proxy=PROXY, raise_exception_on_error=False):
        if not self.base_url:
            raise Exception('Cannot use send_api_request from _HTTP class.')
        base_url = self.base_url.format(endpoint=endpoint)
        endpoint = endpoint.lower()
        headers = self.headers
        if referer:
            headers['Referer'] = referer
        proxies = None
        if proxy:
            proxies = {
                "http": proxy,
                "https": proxy,
            }

        contents = None
        url = None

        if DEBUG and DEBUG_STORAGE:
            print(endpoint, parameters)
            directory_name = 'debug_storage'
            parameter_string = '&'.join('{}={}'.format(key, val) for key, val in sorted(parameters.items())).encode('utf-8')
            file_name = "{}-{}.txt".format(endpoint, md5(parameter_string).hexdigest())
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'debug', directory_name)
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            file_path = os.path.join(file_path, file_name)
            print(file_name, os.path.isfile(file_path))
            if os.path.isfile(file_path):
                f = open(file_path, 'r')
                contents = f.read()
                f.close()
                url = "{}?{}".format(base_url, parameter_string)
                print('loading from file...')

        if not contents:
            response = requests.get(url=base_url, params=parameters, headers=headers, proxies=proxies)
            url = response.url
            contents = response.text

        contents = self.clean_contents(contents)
        if DEBUG and DEBUG_STORAGE:
            f = open(file_path, 'w')
            f.write(contents)
            f.close()

        data = self.nba_response(response=contents, url=url)

        if raise_exception_on_error and not data.valid_json():
            raise Exception('InvalidResponse: Response is not in a valid JSON format.')

        return data
