import json

from fetchr.fetchr_exception import FetchRException


class ApiBase:
    def __init__(self, client):
        self._client = client

    def _request(self, *args):
        return self._client._client.request(*args)


class EntityEndpoints(ApiBase):
    def __init__(self, client, entity):
        super().__init__(client)
        self.entity = entity

    def insert(self, data=..., **kwargs):
        return self.__query("insert", data, kwargs)

    def detail(self, data=..., **kwargs):
        return self.__query("detail", data, kwargs)

    def list(self, data=..., **kwargs):
        return self.__query("list", data, kwargs)

    def list_references(self, data=..., **kwargs):
        return self.__query("refs", data, kwargs)

    def aggregate(self, data=..., **kwargs):
        return self.__query("aggregate", data, kwargs)

    def count(self, data=..., **kwargs):
        return self.__query("count", data, kwargs)

    def update(self, data):
        return self.__query("update", data, None)

    def delete(self, data=..., **kwargs):
        return self.__query("delete", data, kwargs)

    def delete_all(self):
        self.delete({'params': {'all': True}})

    def __query(self, op, data, kwargs):
        if data is ...:
            data = {'params': {**kwargs}}
        return self._request(f"{self.entity}/{op}", data)


class EntityApi(ApiBase):
    def __getitem__(self, entity_name) -> EntityEndpoints:
        return EntityEndpoints(self._client, entity_name)

    def __getattr__(self, attribute) -> EntityEndpoints:
        return self[attribute]


class DatabasesApi(ApiBase):
    def set(self, data=..., **kwargs):
        if data is ...:
            data = kwargs
        return self._request("database/set", data)

    def set_in_memory(self, data=..., **kwargs):
        if data is ...:
            data = kwargs
        return self._request("database/set/mem", data)

    def get(self):
        return self._request("database/get")

    def list(self):
        return self._request("database/list")


class ModelsApi(ApiBase):
    def set_model(self, model, model_id=None):
        if isinstance(self, dict):
            model = json.dumps(model)

        return self._request("model/set", model)

    def set_model_from_files(self, model_file, model_id=None):
        return self.set_model(read_model_from_file(model_file), model_id)

    def get_model(self, model_id=None):
        return self._request("model/get")


class MigrationsApi(ApiBase):
    def apply(self, migrations):
        return self._request("database/migrate", {"migrations": migrations})

    def apply_from_files(self, migrations_path):
        return self.apply(read_migrations_from_files(migrations_path))


def read_model_from_file(file):
    with open(file, 'r') as read_file:
        return json.load(read_file)


def read_migrations_from_files(migrations_path, migrations_format='flyway'):
    from pathlib import Path

    if migrations_format != 'flyway':
        raise FetchRException(f"Migrations format unknown ({migrations_format}).")

    if isinstance(migrations_path, str):
        migrations_path = Path(migrations_path)

    migration_files = migrations_path.glob("*.sql")
    migrations = []
    for migration in migration_files:
        with open(migration, 'r') as f:
            migration_data = f.read()

        migration_name = migration.stem
        migration_version, migration_desc = migration_name.split("__")
        migration_version, migration_index = migration_version.split("_")
        migration_version = migration_version.replace("V", "")

        migrations.append({
            "versionIndex": int(migration_version),
            "sequenceIndex": int(migration_index),
            "label": migration_desc,
            "migration": migration_data,
        })

    return migrations
