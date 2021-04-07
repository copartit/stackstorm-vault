from lib import action


class VaultDeleteAction(action.VaultBaseAction):
    def run(self, path, profile=None):
        self.setup(profile)
        return self.vault.delete(path)
