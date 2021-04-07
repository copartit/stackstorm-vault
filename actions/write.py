import json
from lib import action


class VaultWriteAction(action.VaultBaseAction):
    def run(self, path, values, profile=None):
        self.setup(profile)
        return self.vault.write(path, **json.loads(values))
