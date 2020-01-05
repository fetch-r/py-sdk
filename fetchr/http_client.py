import requests


class HttpApiException(Exception):
    def __init__(self, message, status, response):
        super().__init__(message)

        self.response = response

        self.status = status
        self.message = message

    def __str__(self) -> str:
        return super().__str__()


class HttpApiClientWrapper:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers or {}

    def request(self, uri, data=..., headers=...):
        if data is ...:
            data = {}

        if headers is ...:
            headers = {}

        combined_headers = {**self.headers, **headers}
        endpoint = self.host + "/" + uri

        response = requests.post(
            endpoint,
            json=data,
            headers=combined_headers
        )

        if not response.ok:
            raise HttpApiException(response.json(), response.status_code, response)

        return response.json()

    def with_headers(self, **headers):
        return HttpApiClientWrapper(self.host, headers)
