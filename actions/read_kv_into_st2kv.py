import json

from read_kv import VaultReadKVAction


class VaultReadKVintoST2KVAction(VaultReadKVAction):
    # noinspection PyMethodOverriding
    def run(
        self, st2kv_key, st2kv_ttl, path, kv_version, mount_point, version, profile=None
    ):
        value = super(VaultReadKVintoST2KVAction, self).run(
            path=path,
            kv_version=kv_version,
            mount_point=mount_point,
            version=version,
            profile=profile,
        )
        if not isinstance(str, value):
            try:
                value = json.dumps(value)
            except TypeError:
                value = str(value)
        return self.action_service.set_value(
            name=st2kv_key, value=value, ttl=st2kv_ttl, local=False, encrypt=True
        )
