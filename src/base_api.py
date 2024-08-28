import requests
import logging

class BaseAPI:
    """Base class for handling basic HTTP operations."""
    
    def __init__(self, base_url, api_key=None, logger=None):
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()
        self.logger = logger or logging.getLogger(__name__)

        if self.api_key:
            self.session.params = {'api_key': self.api_key}

    def _log_request(self, method, url, **kwargs):
        self.logger.info(f"Request: {method.upper()} {url}")
        self.logger.debug(f"Params: {kwargs.get('params')}")
        self.logger.debug(f"Data: {kwargs.get('data')}")
        self.logger.debug(f"JSON: {kwargs.get('json')}")

    def _log_response(self, response):
        self.logger.info(f"Response: {response.status_code} - {response.url}")
        self.logger.debug(f"Response body: {response.text}")

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        self._log_request(method, url, **kwargs)
        response = self.session.request(method, url, **kwargs)
        self._log_response(response)
        return response

    def get(self, endpoint, params=None):
        """Send a GET request."""
        return self._request("get", endpoint, params=params)

    def post(self, endpoint, data=None, json=None):
        """Send a POST request."""
        return self._request("post", endpoint, data=data, json=json)

    def put(self, endpoint, data=None, json=None):
        """Send a PUT request."""
        return self._request("put", endpoint, data=data, json=json)

    def delete(self, endpoint, params=None):
        """Send a DELETE request."""
        return self._request("delete", endpoint, params=params)