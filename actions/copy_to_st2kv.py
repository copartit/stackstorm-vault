from read import VaultReadAction


class VaultReadToST2KVAction(VaultReadAction):
    # noinspection PyMethodOverriding
    def run(self, st2kv_key, st2kv_ttl, path, profile=None):
        value = super(VaultReadToST2KVAction, self).run(path=path, profile=profile)
        return self.action_service.set_value(
            name=st2kv_key, value=value, ttl=st2kv_ttl, local=False, encrypt=True
        )
