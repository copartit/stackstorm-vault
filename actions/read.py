from lib import action


class VaultReadAction(action.VaultBaseAction):
    def run(self, path, profile=None):
        self.setup(profile)
        value = self.vault.read(path)
        if value:
            return value['data']
        else:
            raise KeyError("Key was not found in Vault")
