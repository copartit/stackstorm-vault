import json
from write import VaultWriteAction


class VaultWriteIntoST2KVAction(VaultWriteAction):
    # noinspection PyMethodOverriding
    def run(self, st2kv_key, st2kv_ttl, path, values, profile=None):
        output = super(VaultWriteIntoST2KVAction, self).run(
            path=path, values=values, profile=profile
        )
        if not isinstance(str, output):
            try:
                output = json.dumps(output)
            except TypeError:
                output = str(output)
        return self.action_service.set_value(
            name=st2kv_key, value=output, ttl=st2kv_ttl, local=False, encrypt=True
        )
