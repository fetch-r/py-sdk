from .fetchr_apis import *
from .http_client import HttpApiClientWrapper


class FetchRClient:
    def __init__(self, client: HttpApiClientWrapper):
        self._client: HttpApiClientWrapper = client

    def list(self, params):
        return self._client.request("data", params)

    def mutate(self, params):
        return self._client.request("mutate", params)

    def with_headers(self, **headers):
        return FetchRClient(self._client.with_headers(**headers))

    def with_model_id(self, model_id):
        return self.with_headers(model=model_id)

    @property
    def entities(self) -> EntityApi:
        return EntityApi(self)

    @property
    def database_api(self):
        return DatabasesApi(self)

    @property
    def models_api(self):
        return ModelsApi(self)

    @property
    def migrations_api(self):
        return MigrationsApi(self)

    @staticmethod
    def connect(host):
        return FetchRClient(client=HttpApiClientWrapper(host))
