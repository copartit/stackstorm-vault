import json

from read import VaultReadAction


class VaultReadIntoST2KVAction(VaultReadAction):
    # noinspection PyMethodOverriding
    def run(self, st2kv_key, st2kv_ttl, path, profile=None):
        value = super(VaultReadIntoST2KVAction, self).run(path=path, profile=profile)
        if not isinstance(value, str):
            try:
                value = json.dumps(value)
            except TypeError:
                value = str(value)
        return self.action_service.set_value(
            name=st2kv_key, value=value, ttl=st2kv_ttl, local=False, encrypt=True
        )
